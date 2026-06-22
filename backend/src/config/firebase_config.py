import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth as firebase_auth
import os
from src.config.settings import settings

_db = None
_auth = None

def initialize_firebase():
    global _db, _auth
    
    try:
        # Check if already initialized
        firebase_admin.get_app()
    except ValueError:
        # Initialize Firebase
        cred_dict = {
            "type": "service_account",
            "project_id": settings.FIREBASE_PROJECT_ID,
            "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
            "private_key": settings.FIREBASE_PRIVATE_KEY.replace('\\n', '\n'),
            "client_email": settings.FIREBASE_CLIENT_EMAIL,
            "client_id": os.getenv("FIREBASE_CLIENT_ID"),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL")
        }
        
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
    
    _db = firestore.client()
    _auth = firebase_auth
    
    return _db, _auth

def get_db():
    return _db

def get_auth():
    return _auth
