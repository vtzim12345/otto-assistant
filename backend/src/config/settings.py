from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # App
    APP_NAME: str = "OTTO"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    PORT: int = 8000
    
    # Firebase
    FIREBASE_PROJECT_ID: str = Field(default="", env="FIREBASE_PROJECT_ID")
    FIREBASE_PRIVATE_KEY: str = Field(default="", env="FIREBASE_PRIVATE_KEY")
    FIREBASE_CLIENT_EMAIL: str = Field(default="", env="FIREBASE_CLIENT_EMAIL")
    
    # AI APIs (Required)
    OPENAI_API_KEY: str = Field(default="", env="OPENAI_API_KEY")
    GROQ_API_KEY: str = Field(default="", env="GROQ_API_KEY")
    GOOGLE_API_KEY: str = Field(default="", env="GOOGLE_API_KEY")
    
    # Voice & Vision
    ELEVENLABS_API_KEY: str = Field(default="", env="ELEVENLABS_API_KEY")
    GOOGLE_VISION_API_KEY: str = Field(default="", env="GOOGLE_VISION_API_KEY")
    
    # OAuth
    GOOGLE_CLIENT_ID: str = Field(default="", env="GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = Field(default="", env="GOOGLE_CLIENT_SECRET")
    
    # JWT
    JWT_SECRET: str = Field(default="otto-secret-key", env="JWT_SECRET")
    JWT_EXPIRY: str = Field(default="7d", env="JWT_EXPIRY")
    
    # Email
    SUPPORT_EMAIL: str = "suporte.dev.victor@gmail.com"
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:8081",
        "http://10.0.2.2:8000",  # Android emulator
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
