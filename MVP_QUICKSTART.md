# OTTO - MVP Quick Start Guide

## 🎯 MVP Focus

**Only Essential Features:**
- ✅ User Authentication (Login/Register)
- ✅ Chat Interface
- ✅ AI Integration (OpenAI)
- ✅ Message History
- ✅ Basic Settings

**NOT Implemented Yet:**
- ❌ Voice Features
- ❌ Vision Features
- ❌ Projects
- ❌ Reminders
- ❌ Integrations
- ❌ Advanced Features

---

## 🔧 Backend Setup

### 1. Create Virtual Environment
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp ../.env.example .env
```

Edit `.env` and add:
```
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_PRIVATE_KEY=your_private_key
FIREBASE_CLIENT_EMAIL=your_client_email
OPENAI_API_KEY=sk-your-key-here
```

### 4. Run Backend
```bash
python main.py
```

Test: http://localhost:8000/health

---

## 📱 Mobile App Setup

### 1. Install Dependencies
```bash
cd mobile
npm install
```

### 2. Configure API URL

Edit `mobile/src/config/api.ts`:
```typescript
// For Android Emulator:
export const API_URL = 'http://10.0.2.2:8000';

// For Physical Device:
// export const API_URL = 'http://YOUR_IP:8000';

// For iOS Simulator:
// export const API_URL = 'http://localhost:8000';
```

### 3. Run on Android
```bash
npm run android
```

### 4. Run on iOS
```bash
npm run ios
```

### 5. Or Use Expo
```bash
npm start
# Scan QR code with Expo Go app
```

---

## 📋 MVP Features

### Backend Endpoints

#### Authentication
```
POST /auth/register
POST /auth/login
POST /auth/google
POST /auth/apple
POST /auth/github
```

#### Chat
```
POST /chat/message        # Send message & get response
GET  /chat/history        # Get conversation history
GET  /chat/conversation/{id}
DELETE /chat/conversation/{id}
```

#### Settings
```
GET  /settings
PUT  /settings
```

### Mobile Features

- **Login Screen**: Email, Password, Social Auth
- **Chat Screen**: Send/Receive messages, Loading state
- **Settings Screen**: Logout, Language, API info
- **Token Persistence**: Auto-login on app restart

---

## 🧪 Testing Checklist

### Backend
- [ ] Health check endpoint responds
- [ ] Registration creates user in Firebase
- [ ] Login returns valid JWT token
- [ ] Chat endpoint calls OpenAI successfully
- [ ] Messages save to Firestore
- [ ] Error handling works

### Mobile
- [ ] App launches without crashes
- [ ] Login screen displays correctly
- [ ] Registration works
- [ ] Login with email works
- [ ] Chat messages send successfully
- [ ] AI responses display
- [ ] Settings screen accessible
- [ ] Logout works

---

## 🐛 Troubleshooting

### Backend Won't Start
```bash
# Check Python version (need 3.9+)
python --version

# Reinstall dependencies
pip install -r requirements.txt

# Clear cache
pip cache purge
```

### Mobile Can't Connect to Backend

**Android Emulator:**
- Use `http://10.0.2.2:8000` (not localhost)
- Check firewall

**Physical Device:**
- Use your computer's IP (e.g., `http://192.168.1.100:8000`)
- Ensure on same WiFi

**iOS Simulator:**
- Use `http://localhost:8000`

### Firebase Authentication Fails
- Check `.env` credentials are correct
- Verify Firebase project exists
- Enable Email/Google/Apple/GitHub in Firebase Console

### OpenAI API Not Responding
- Verify `OPENAI_API_KEY` is correct
- Check API key has sufficient credits
- Test API key directly: `curl https://api.openai.com/v1/models -H "Authorization: Bearer sk-..."`

---

## 📊 Project Structure

```
otto-assistant/
├── backend/
│   ├── src/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── auth.py      # Authentication
│   │   │       └── chat.py      # Chat with AI
│   │   ├── config/
│   │   │   ├── settings.py      # Config
│   │   │   └── firebase_config.py
│   │   └── models/
│   │       └── schemas.py       # Data models
│   ├── requirements.txt
│   └── main.py                  # FastAPI app
│
├── mobile/
│   ├── src/
│   │   ├── screens/
│   │   │   ├── LoginScreen.tsx
│   │   │   ├── ChatScreen.tsx
│   │   │   └── SettingsScreen.tsx
│   │   ├── services/
│   │   │   └── api.ts           # API calls
│   │   ├── contexts/
│   │   │   └── AuthContext.tsx
│   │   └── hooks/
│   │       └── useAuth.ts
│   ├── App.tsx
│   ├── app.json
│   └── package.json
│
└── docs/
    ├── MVP_QUICKSTART.md        # This file
    ├── API.md
    └── SETUP.md
```

---

## ⚙️ Environment Variables

### Backend (.env)
```
# Firebase
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_PRIVATE_KEY=your_private_key
FIREBASE_CLIENT_EMAIL=your_client_email
FIREBASE_PRIVATE_KEY_ID=your_key_id
FIREBASE_CLIENT_ID=your_client_id
FIREBASE_CLIENT_X509_CERT_URL=your_cert_url

# OpenAI
OPENAI_API_KEY=sk-...

# JWT
JWT_SECRET=your-secret-key

# App
DEBUG=True
PORT=8000
```

---

## 🚀 Deployment (Future)

### Backend
- [ ] Deploy to Heroku / Railway / Render
- [ ] Set up CI/CD pipeline
- [ ] Configure production environment

### Mobile
- [ ] Build for Android (APK/AAB)
- [ ] Build for iOS (IPA)
- [ ] Deploy to Play Store
- [ ] Deploy to App Store

---

## 📞 Support

**Email:** suporte.dev.victor@gmail.com

---

## 📝 Version

- **Version:** 1.0.0 (MVP)
- **Created by:** Victor G.
- **Date:** 2024

---

## ✅ Completion Status

- [x] Backend API setup
- [x] Authentication system
- [x] Chat with AI
- [x] Message history
- [x] Mobile app skeleton
- [x] Login/Chat/Settings screens
- [ ] Testing & debugging
- [ ] Performance optimization
- [ ] Deployment

**Next Phase:** Advanced features (Voice, Vision, Projects, etc.)
