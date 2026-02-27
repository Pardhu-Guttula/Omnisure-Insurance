# Epic Title: As a policyholder, I want to track my claims in the account management module so that I can see the status and details of my claims.

from flask import Blueprint, jsonify, request
from backend.database import get_db_connection

claim_bp = Blueprint('claim', __name__)

@claim_bp.route('/claims', methods=['GET'])
def get_claims():
    account_id = request.args.get('account_id', type=int)
    if not account_id:
        return jsonify({'error': 'Account ID is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Claim WHERE account_id = %s', (account_id,))
    claims = cursor.fetchall()
    cursor.close()
    conn.close()

    if not claims:
        return jsonify({'message': 'No claims found'}), 404

    claim_list = []
    for claim in claims:
        claim_list.append({
            'claim_id': claim[0],
            'policy_id': claim[1],
            'amount': claim[3],
            'status': claim[4],
            'date_filed': claim[5],
            'resolution': claim[6]
        })

    return jsonify({'claims': claim_list}), 200

@claim_bp.route('/claims/<int:claim_id>', methods=['GET'])
def get_claim_details(claim_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Claim WHERE claim_id = %s', (claim_id,))
    claim = cursor.fetchone()
    cursor.close()
    conn.close()

    if not claim:
        return jsonify({'error': 'Claim not found'}), 404

    claim_details = {
        'claim_id': claim[0],
        'policy_id': claim[1],
        'account_id': claim[2],
        'amount': claim[3],
        'status': claim[4],
        'date_filed': claim[5],
        'resolution': claim[6]
    }

    return jsonify({'claim': claim_details}), 200