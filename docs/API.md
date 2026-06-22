# 🔌 OTTO - API Reference

## Base URL
```
http://localhost:8000
```

## Authentication
All endpoints (except `/auth/*`) require a JWT token in the header:
```
Authorization: Bearer <JWT_TOKEN>
```

---

## 🔐 Authentication Endpoints

### POST /auth/register
Create a new account
```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "User Name"
}
```
Response: 201
```json
{
  "token": "jwt_token_here",
  "user": {
    "id": "user_id",
    "email": "user@example.com",
    "name": "User Name"
  }
}
```

### POST /auth/login
Login with email and password
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```
Response: 200
```json
{
  "token": "jwt_token_here",
  "user": { ... }
}
```

### POST /auth/google
Login with Google token
```json
{
  "token": "google_id_token"
}
```

### POST /auth/apple
Login with Apple token
```json
{
  "token": "apple_id_token"
}
```

### POST /auth/github
Login with GitHub token
```json
{
  "token": "github_token"
}
```

---

## 💬 Chat Endpoints

### POST /chat/message
Send a chat message
```json
{
  "message": "What's the weather?",
  "project_id": "project_123",
  "language": "pt-BR"
}
```
Response: 200
```json
{
  "response": "The weather is...",
  "conversation_id": "conv_123",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### GET /chat/history
Get conversation history
```
Query params:
- limit=20
- offset=0
- project_id=project_123 (optional)
```
Response: 200
```json
{
  "conversations": [
    {
      "id": "conv_123",
      "messages": [...],
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

### GET /chat/conversation/{id}
Get specific conversation

Response: 200
```json
{
  "id": "conv_123",
  "title": "Weather Discussion",
  "messages": [
    {
      "role": "user",
      "content": "What's the weather?",
      "timestamp": "2024-01-01T00:00:00Z"
    },
    {
      "role": "assistant",
      "content": "The weather is...",
      "timestamp": "2024-01-01T00:00:01Z"
    }
  ]
}
```

### DELETE /chat/conversation/{id}
Delete a conversation

Response: 204 (No Content)

### PUT /chat/conversation/{id}
Update conversation (e.g., title)
```json
{
  "title": "New Title"
}
```

---

## 🎤 Voice Endpoints

### POST /voice/transcribe
Convert speech to text
```
Body: audio file (multipart/form-data)
```
Response: 200
```json
{
  "text": "What's the weather?",
  "confidence": 0.95,
  "language": "pt-BR"
}
```

### POST /voice/synthesize
Convert text to speech
```json
{
  "text": "The weather is sunny.",
  "voice": "male_br",
  "accent": "brazil",
  "speed": 1.0
}
```
Response: 200
```
Body: audio file (audio/mpeg)
```

### GET /voice/voices
Get available voices

Response: 200
```json
{
  "voices": [
    {
      "id": "male_br",
      "name": "João",
      "language": "pt-BR",
      "accent": "Brazil"
    },
    {
      "id": "female_br",
      "name": "Maria",
      "language": "pt-BR",
      "accent": "Brazil"
    }
  ]
}
```

---

## 👁️ Vision Endpoints

### POST /vision/analyze-image
Analyze an image
```
Body: image file (multipart/form-data)
```
Response: 200
```json
{
  "description": "Image description...",
  "objects": ["object1", "object2"],
  "text": "Any text in the image",
  "confidence": 0.98
}
```

### POST /vision/analyze-webcam
Analyze webcam stream
```
Body: video frame (multipart/form-data)
```
Response: 200
```json
{
  "objects": [...],
  "people": 1,
  "scene": "Office"
}
```

### POST /vision/generate-image
Generate an image
```json
{
  "prompt": "A beautiful sunset over the ocean",
  "style": "realistic",
  "size": "1024x1024"
}
```
Response: 200
```json
{
  "url": "https://...",
  "prompt": "A beautiful sunset..."
}
```

---

## 📋 Projects Endpoints

### POST /projects
Create a new project
```json
{
  "name": "My Project",
  "icon": "📚",
  "color": "#FF5733",
  "description": "Project description"
}
```
Response: 201
```json
{
  "id": "project_123",
  "name": "My Project",
  "icon": "📚",
  "color": "#FF5733"
}
```

### GET /projects
Get all projects

Response: 200
```json
{
  "projects": [...]
}
```

### PUT /projects/{id}
Update project

### DELETE /projects/{id}
Delete project

---

## ⏰ Reminders & Alarms Endpoints

### POST /reminders
Create a reminder
```json
{
  "title": "Meeting",
  "description": "Team meeting",
  "scheduled_time": "2024-01-01T14:00:00Z",
  "recurring": "daily"
}
```

### GET /reminders
Get all reminders

### DELETE /reminders/{id}
Delete reminder

---

## ⚙️ Settings Endpoints

### GET /settings
Get user settings

Response: 200
```json
{
  "theme": "dark",
  "language": "pt-BR",
  "wake_word": "otto",
  "voice": "male_br",
  "notifications_enabled": true
}
```

### PUT /settings
Update settings
```json
{
  "theme": "light",
  "language": "en",
  "wake_word": "hey"
}
```

---

## ❤️ Health Check

### GET /health
Check API status

Response: 200
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid request",
  "message": "Field 'email' is required"
}
```

### 401 Unauthorized
```json
{
  "error": "Unauthorized",
  "message": "Invalid or missing token"
}
```

### 404 Not Found
```json
{
  "error": "Not found",
  "message": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error",
  "message": "Something went wrong"
}
```

---

**Created by Victor G. © 2024**
