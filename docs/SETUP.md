# 🚀 OTTO - Setup Guide

## 📋 Prerequisites

### Global Requirements
- Node.js 16+ (for mobile development)
- Git
- A Firebase project (free tier is fine)
- API keys:
  - OpenAI (free trial available)
  - ElevenLabs (free tier available)
  - Google Cloud APIs (free tier available)

### For Android
- Android SDK
- Java 11+
- Android Studio (recommended)
- Physical device or emulator

### For iOS (macOS only)
- Xcode 13+
- CocoaPods
- Apple Developer Account (for publishing)
- Physical device or simulator

### For Backend
- Python 3.9+
- pip
- Virtual environment

---

## 🔧 Step-by-Step Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/vtzim12345/otto-assistant.git
cd otto-assistant
```

### Step 2: Backend Setup

#### 2.1 Create Virtual Environment
```bash
cd backend
python -m venv venv

# Activate (choose your OS)
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

#### 2.2 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 2.3 Configure Environment
```bash
cp .env.example .env
```

#### 2.4 Set Up Firebase
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project
3. Enable:
   - Authentication (Google, Apple, Email/Password, GitHub)
   - Firestore Database (use India or US region)
   - Cloud Storage
4. Download service account JSON
5. Add credentials to .env

#### 2.5 Add API Keys
Edit `.env` and add:
```
OPENAI_API_KEY=sk-...
GROQ_API_KEY=gsk_...
GOOGLE_API_KEY=...
ELEVENLABS_API_KEY=...
```

#### 2.6 Run Backend
```bash
python main.py
# Server runs on http://localhost:8000
```

---

### Step 3: Mobile App Setup

#### 3.1 Install Dependencies
```bash
cd ../mobile
npm install
```

#### 3.2 Configure Firebase (React Native)
```bash
# Copy Google services files
cp google-services.json android/app/  # For Android
cp GoogleService-Info.plist ios/      # For iOS (if available)
```

#### 3.3 Update Backend URL
Edit `mobile/src/config/api.ts`:
```typescript
export const API_URL = 'http://YOUR_BACKEND_IP:8000';
// For local testing:
// Android: http://10.0.2.2:8000
// iOS: http://localhost:8000
```

#### 3.4 Run on Android
```bash
npm run android
# or
react-native run-android
```

#### 3.5 Run on iOS (macOS)
```bash
npm run ios
# or
react-native run-ios
```

---

## 🎯 First Launch

### On the Mobile App:

1. **Sign Up**
   - Choose authentication method (Google, Email, etc)
   - Create account
   - Complete profile

2. **Permissions**
   - Grant microphone access
   - Grant camera access (for vision features)
   - Grant notification access

3. **Configure APIs**
   - Go to Settings > APIs
   - Test connection to backend
   - Verify all APIs are responding

4. **Set Wake Word**
   - Settings > Voice > Wake Word
   - Record your custom wake word

5. **Choose Voice**
   - Settings > Voice > Voice Selection
   - Listen to samples
   - Choose favorite

6. **First Chat**
   - Say "Hi Otto" or start typing
   - See the 3D orb animation
   - Have a conversation!

---

## 📱 Testing Checklist

- [ ] Backend API responding on `/health`
- [ ] Firebase authentication working
- [ ] App connects to backend
- [ ] Login works
- [ ] Chat sends/receives messages
- [ ] Voice activation works
- [ ] 3D orb animates
- [ ] Messages save to Firebase
- [ ] Settings are persistent

---

## 🐛 Troubleshooting

### Backend Issues

**Python version error**
```bash
# Use Python 3.9+
python --version
```

**Firebase connection error**
- Check .env file
- Verify credentials are correct
- Ensure Firebase project exists

**Port already in use**
```bash
# Change PORT in .env
PORT=8001
```

### Mobile Issues

**Can't connect to backend (Android)**
- Use `http://10.0.2.2:8000` instead of `localhost`
- Check firewall settings
- Ensure backend is running

**Can't connect to backend (iOS)**
- Use `http://localhost:8000`
- Check WiFi connection
- Restart app and backend

**Microphone not working**
- Grant permissions in app settings
- Check system permissions
- Restart app

**Build fails**
```bash
# Clear cache and rebuild
rm -rf node_modules
npm install
npm start -- --reset-cache
```

---

## 📚 Next Steps

1. **Read [FEATURES.md](./FEATURES.md)** to learn all features
2. **Read [API.md](./API.md)** for backend endpoints
3. **Check [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)** if you have issues
4. **Join the community** for support

---

## 💬 Need Help?

📧 **Email:** suporte.dev.victor@gmail.com

---

**Created by Victor G. © 2024**
