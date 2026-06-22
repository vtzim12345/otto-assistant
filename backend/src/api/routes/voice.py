from fastapi import APIRouter, Depends, File, UploadFile
from src.api.routes.auth import verify_token
from src.config.settings import settings
from elevenlabs import client as elevenlabs_client
from elevenlabs.client import ElevenLabs
import speech_recognition as sr

router = APIRouter()

elevenlabs = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)

@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...), user_id: str = Depends(verify_token)):
    """Convert speech to text using Google Speech Recognition"""
    try:
        recognizer = sr.Recognizer()
        audio_data = await file.read()
        
        # Process audio (simplified)
        with sr.AudioFile(file.filename) as source:
            audio = recognizer.record(source)
        
        text = recognizer.recognize_google(audio, language="pt-BR")
        
        return {
            "text": text,
            "confidence": 0.95,
            "language": "pt-BR"
        }
    except Exception as e:
        return {"error": str(e)}

@router.post("/synthesize")
async def synthesize_speech(text: str, voice: str = "male_br", user_id: str = Depends(verify_token)):
    """Convert text to speech using ElevenLabs"""
    try:
        audio = elevenlabs.generate(
            text=text,
            voice=voice,
            model="eleven_monolingual_v1"
        )
        
        return audio
    except Exception as e:
        return {"error": str(e)}

@router.get("/voices")
async def get_available_voices(user_id: str = Depends(verify_token)):
    """Get available voices"""
    voices = [
        {
            "id": "male_br",
            "name": "João",
            "language": "pt-BR",
            "accent": "Brazil",
            "gender": "male"
        },
        {
            "id": "female_br",
            "name": "Maria",
            "language": "pt-BR",
            "accent": "Brazil",
            "gender": "female"
        },
        {
            "id": "male_en",
            "name": "John",
            "language": "en-US",
            "accent": "US",
            "gender": "male"
        },
        {
            "id": "female_en",
            "name": "Emma",
            "language": "en-US",
            "accent": "US",
            "gender": "female"
        }
    ]
    
    return {"voices": voices}
