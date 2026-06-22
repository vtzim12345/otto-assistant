from fastapi import APIRouter, Depends, HTTPException
from src.config.firebase_config import get_db
from src.api.routes.auth import verify_token

router = APIRouter()

@router.get("/")
async def get_settings(user_id: str = Depends(verify_token)):
    """Get user settings"""
    try:
        db = get_db()
        
        user_doc = db.collection('users').document(user_id).get()
        if not user_doc.exists:
            raise HTTPException(status_code=404, detail="User not found")
        
        user_data = user_doc.to_dict()
        settings = user_data.get('settings', {})
        
        return settings
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/")
async def update_settings(settings_data: dict, user_id: str = Depends(verify_token)):
    """Update user settings"""
    try:
        db = get_db()
        
        db.collection('users').document(user_id).update({
            'settings': settings_data
        })
        
        return {'message': 'Settings updated', 'settings': settings_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
