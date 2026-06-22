from fastapi import APIRouter, Depends, HTTPException
from src.models.schemas import ChatMessage, ChatResponse
from src.config.firebase_config import get_db
from src.api.routes.auth import verify_token
from datetime import datetime
import openai
from src.config.settings import settings

router = APIRouter()

openai.api_key = settings.OPENAI_API_KEY

@router.post("/message", response_model=ChatResponse)
async def send_message(message_data: ChatMessage, user_id: str = Depends(verify_token)):
    """Send a chat message and get AI response"""
    try:
        db = get_db()
        
        # Get or create conversation
        if message_data.project_id:
            conv_ref = db.collection('conversations').document(message_data.project_id)
        else:
            conv_ref = db.collection('conversations').add({
                'user_id': user_id,
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            })[1]
        
        # Store user message
        db.collection('messages').add({
            'conversation_id': conv_ref.id if hasattr(conv_ref, 'id') else message_data.project_id,
            'user_id': user_id,
            'role': 'user',
            'content': message_data.message,
            'timestamp': datetime.now()
        })
        
        # Get AI response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message_data.message}],
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        # Store AI response
        db.collection('messages').add({
            'conversation_id': conv_ref.id if hasattr(conv_ref, 'id') else message_data.project_id,
            'role': 'assistant',
            'content': ai_response,
            'timestamp': datetime.now()
        })
        
        return ChatResponse(
            response=ai_response,
            conversation_id=conv_ref.id if hasattr(conv_ref, 'id') else message_data.project_id,
            timestamp=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history")
async def get_history(user_id: str = Depends(verify_token), limit: int = 20, offset: int = 0):
    """Get conversation history"""
    try:
        db = get_db()
        
        conversations = db.collection('conversations')\
            .where('user_id', '==', user_id)\
            .order_by('created_at', direction='DESCENDING')\
            .limit(limit)\
            .stream()
        
        result = []
        for conv in conversations:
            result.append({
                'id': conv.id,
                'data': conv.to_dict()
            })
        
        return {'conversations': result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/conversation/{conversation_id}")
async def delete_conversation(conversation_id: str, user_id: str = Depends(verify_token)):
    """Delete a conversation"""
    try:
        db = get_db()
        db.collection('conversations').document(conversation_id).delete()
        return {"message": "Conversation deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
