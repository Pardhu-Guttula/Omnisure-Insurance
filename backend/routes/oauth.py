# Epic Title: OAuth Integration for Social Logins

from flask import Blueprint, request, jsonify, redirect, url_for
from backend.models.user import User
from backend.models.oauth import OAuth
from backend.models.session import Session
from backend.database import get_db_connection
from oauthlib.oauth2 import WebApplicationClient
import requests

oauth_bp = Blueprint('oauth', __name__)

client_id = "your_client_id"
client_secret = "your_client_secret"
discovery_url = "https://accounts.google.com/.well-known/openid-configuration"
client = WebApplicationClient(client_id)

def get_google_provider_cfg():
    return requests.get(discovery_url).json()

@oauth_bp.route("/login")
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@oauth_bp.route("/login/callback")
def callback():
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(client_id, client_secret),
    )
    client.parse_request_body_response(token_response.text)
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        email = userinfo_response.json()["email"]
        unique_id = userinfo_response.json()["sub"]
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute('SELECT * FROM User WHERE email = %s', (email,))
        user_record = cursor.fetchone()
        
        if not user_record:
            new_user = User(email)
            cursor.execute(
                'INSERT INTO User (email) VALUES (%s)',
                (new_user.email,)
            )
            user_id = cursor.lastrowid
        else:
            user_id = user_record['id']
        
        cursor.execute('SELECT * FROM OAuth WHERE oauth_provider = %s AND oauth_id = %s', ('google', unique_id))
        oauth_record = cursor.fetchone()
        
        if not oauth_record:
            cursor.execute(
                'INSERT INTO OAuth (oauth_provider, oauth_id, user_id) VALUES (%s, %s, %s)',
                ('google', unique_id, user_id)
            )
        
        session = Session(user_id)
        cursor.execute(
            'INSERT INTO Session (session_id, user_id) VALUES (%s, %s)',
            (session.session_id, session.user_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({'message': 'OAuth login successful', 'session_token': session.session_id}), 200
    
    return jsonify({'error': 'User email not available or not verified by OAuth provider'}), 400