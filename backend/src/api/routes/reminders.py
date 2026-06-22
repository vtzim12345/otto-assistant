from fastapi import APIRouter, Depends, HTTPException
from src.models.schemas import ReminderCreate
from src.config.firebase_config import get_db
from src.api.routes.auth import verify_token
from datetime import datetime

router = APIRouter()

@router.post("/")
async def create_reminder(reminder_data: ReminderCreate, user_id: str = Depends(verify_token)):
    """Create a reminder"""
    try:
        db = get_db()
        
        reminder = {
            'user_id': user_id,
            'title': reminder_data.title,
            'description': reminder_data.description,
            'scheduled_time': reminder_data.scheduled_time,
            'recurring': reminder_data.recurring,
            'created_at': datetime.now(),
            'completed': False
        }
        
        db.collection('reminders').add(reminder)
        
        return {'message': 'Reminder created', 'reminder': reminder}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def get_reminders(user_id: str = Depends(verify_token)):
    """Get all reminders for user"""
    try:
        db = get_db()
        
        reminders = db.collection('reminders')\
            .where('user_id', '==', user_id)\
            .stream()
        
        result = []
        for rem in reminders:
            result.append({
                'id': rem.id,
                **rem.to_dict()
            })
        
        return {'reminders': result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
