from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class AuthResponse(BaseModel):
    token: str
    user: User

class ChatMessage(BaseModel):
    message: str
    project_id: Optional[str] = None
    language: str = "pt-BR"

class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    timestamp: datetime

class ProjectCreate(BaseModel):
    name: str
    icon: Optional[str] = "📁"
    color: Optional[str] = "#6366F1"
    description: Optional[str] = None

class ReminderCreate(BaseModel):
    title: str
    description: Optional[str] = None
    scheduled_time: datetime
    recurring: Optional[str] = None
