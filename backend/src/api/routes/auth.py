from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from firebase_admin import auth as firebase_auth
import jwt
from datetime import datetime, timedelta
from src.config.settings import settings
from src.config.firebase_config import get_db, get_auth
from src.models.schemas import UserCreate, LoginRequest, AuthResponse, User

router = APIRouter()
security = HTTPBearer()

@router.post("/register", response_model=AuthResponse)
async def register(user_data: UserCreate):
    """Create a new account"""
    try:
        db = get_db()
        
        # Create user in Firebase Auth
        user = firebase_auth.create_user(
            email=user_data.email,
            password=user_data.password,
            display_name=user_data.name
        )
        
        # Store user data in Firestore
        db.collection('users').document(user.uid).set({
            'email': user_data.email,
            'name': user_data.name,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        })
        
        # Create JWT token
        token = create_access_token(user.uid)
        
        return AuthResponse(
            token=token,
            user=User(
                id=user.uid,
                email=user_data.email,
                name=user_data.name,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
        )
    except firebase_auth.EmailAlreadyExistsError:
        raise HTTPException(status_code=400, detail="Email already registered")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=AuthResponse)
async def login(credentials: LoginRequest):
    """Login with email and password"""
    try:
        # For demo purposes - in production use Firebase REST API
        db = get_db()
        user_query = db.collection('users').where('email', '==', credentials.email).stream()
        
        user_doc = None
        for doc in user_query:
            user_doc = doc
            break
        
        if not user_doc:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        # Create JWT token
        token = create_access_token(user_doc.id)
        user_data = user_doc.to_dict()
        
        return AuthResponse(
            token=token,
            user=User(
                id=user_doc.id,
                email=user_data['email'],
                name=user_data['name'],
                created_at=user_data['created_at'],
                updated_at=user_data['updated_at']
            )
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/google")
async def google_login(token: str):
    """Login with Google OAuth"""
    try:
        # Verify Google token
        decoded_token = firebase_auth.verify_id_token(token)
        uid = decoded_token['uid']
        
        # Create JWT token
        jwt_token = create_access_token(uid)
        
        return {"token": jwt_token, "uid": uid}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Google token")

@router.post("/apple")
async def apple_login(token: str):
    """Login with Apple ID"""
    try:
        decoded_token = firebase_auth.verify_id_token(token)
        uid = decoded_token['uid']
        jwt_token = create_access_token(uid)
        return {"token": jwt_token, "uid": uid}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Apple token")

@router.post("/github")
async def github_login(token: str):
    """Login with GitHub"""
    try:
        decoded_token = firebase_auth.verify_id_token(token)
        uid = decoded_token['uid']
        jwt_token = create_access_token(uid)
        return {"token": jwt_token, "uid": uid}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid GitHub token")

def create_access_token(user_id: str, expires_delta: timedelta = None):
    """Create JWT token"""
    if expires_delta is None:
        expires_delta = timedelta(days=7)
    
    expire = datetime.utcnow() + expires_delta
    to_encode = {"user_id": user_id, "exp": expire}
    
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm="HS256")
    return encoded_jwt

def verify_token(credentials: HTTPAuthCredentials = Depends(security)):
    """Verify JWT token"""
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
