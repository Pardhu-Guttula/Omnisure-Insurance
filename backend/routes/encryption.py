# Epic Title: As a data engineer, I want data encryption in the PostgreSQL database, so that sensitive data is protected at rest.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection
import logging
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

encryption_bp = Blueprint('encryption', __name__)

# Logging setup for structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('encryption')

# Constants
KEY_LENGTH = 32
PBKDF2_SALT = b'some_salt'
ITERATIONS = 100000
ENC_ALGO = 'AES'

# Secret Key (should be securely stored and rotated)
SECRET_KEY = get_random_bytes(KEY_LENGTH)

def encrypt(data: str) -> str:
    password = SECRET_KEY
    salt = PBKDF2_SALT
    key = PBKDF2(password, salt, dkLen=32, count=ITERATIONS)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    encrypted_data = base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')
    return encrypted_data

def decrypt(encrypted_data: str) -> str:
    password = SECRET_KEY
    salt = PBKDF2_SALT
    key = PBKDF2(password, salt, dkLen=32, count=ITERATIONS)
    data = base64.b64decode(encrypted_data)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')
    return decrypted_data

@encryption_bp.route('/encrypt', methods=['POST'])
def encrypt_data():
    raw_data = request.json.get('data')
    if not raw_data:
        return jsonify({'error': 'No data provided'}), 400
    
    encrypted_data = encrypt(raw_data)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Data (encrypted_data) VALUES (%s)", (encrypted_data,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Data encrypted and stored successfully'}), 200

@encryption_bp.route('/data/<int:data_id>', methods=['GET'])
def retrieve_data(data_id):
    role = request.headers.get('Role')
    
    if role not in ['admin', 'analyst']:
        return jsonify({'error': 'Access denied'}), 403
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT encrypted_data FROM Data WHERE data_id = %s", (data_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not result:
        return jsonify({'error': 'Data not found'}), 404
    
    decrypted_data = decrypt(result[0])
    return jsonify({'data': decrypted_data}), 200