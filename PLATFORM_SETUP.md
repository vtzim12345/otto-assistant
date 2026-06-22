# 📱 OTTO - Setup por Plataforma

## 🚀 MVP - Mobile First (React Native)

### 📲 Android
```bash
# Requisitos
- Node.js 16+
- Java 11+
- Android SDK
- Android Studio

# Setup
cd mobile
npm install
npm run android

# Ou via Expo
npm start
# Digitalize o QR code com Expo Go
```

### 🍎 iOS (macOS only)
```bash
# Requisitos
- macOS 12+
- Xcode 13+
- CocoaPods

# Setup
cd mobile
npm install
cd ios
pod install
cd ..
npm run ios
```

### 💻 Backend (FastAPI)
```bash
# Requisitos
- Python 3.9+
- pip

# Setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure .env
cp .env.example .env
# Adicione suas chaves de API

# Execute
python main.py
# API estará em http://localhost:8000
```

---

## 🔄 Como os Dados Sincronizam

```
┌─────────────┐
│   Mobile    │
│  (React     │
│  Native)    │
└──────┬──────┘
       │
       │ HTTP/WebSocket
       ↓
┌─────────────────────┐
│  FastAPI Backend    │
│   (Python)          │
└──────┬──────────────┘
       │
       │ Firestore API
       ↓
┌──────────────────────┐
│  Firebase Firestore  │
│    (Cloud DB)        │
└──────────────────────┘
```

**Fluxo:**
1. Usuário faz login no app
2. Credenciais são verificadas no Firebase
3. Token JWT é gerado
4. Todas as requisições usam esse token
5. Dados são salvos no Firestore
6. Sincronizam automaticamente entre devices

---

## 🔐 Login - Funciona em Todos os Devices

```
1. Abra OTTO (em qualquer plataforma)
2. Clique em "Entrar" ou "Cadastrar"
3. Escolha um método:
   ✅ Google
   ✅ Apple ID
   ✅ Email + Senha
   ✅ GitHub
4. Faça login
5. Acesse em outro device com a mesma conta
6. Todos seus dados estão sincronizados! 🎉
```

---

## 💾 Dados Sincronizados

- ✅ Histórico de conversas
- ✅ Lembretes e alarmes
- ✅ Projetos
- ✅ Preferências (voz, tema, idioma, wake word)
- ✅ Integrações conectadas
- ✅ APIs customizadas
- ✅ Documentos criados
- ✅ Imagens analisadas

---

## ⚙️ Configuração Inicial

### 1️⃣ Criar Conta
```
1. Abra OTTO
2. Clique em "Cadastrar"
3. Escolha método de autenticação
4. Complete seu perfil
```

### 2️⃣ Configurar APIs (Opcional)
```
1. Vá para ⚙️ Configurações > APIs
2. Adicione suas chaves:
   - OpenAI (recomendado)
   - Groq (alternativo)
   - Google Vision (para imagens)
3. Teste a conexão
```

### 3️⃣ Personalizar Wake Word
```
1. ⚙️ Configurações > Voz
2. Clique em "Wake Word"
3. Digite sua palavra (ex: "Otto", "Hey")
4. Teste e confirme
```

### 4️⃣ Escolher Voz
```
1. ⚙️ Configurações > Voz > Teste de Vozes
2. Escute as opções disponíveis
3. Selecione sua favorita
4. Configure sotaque e velocidade
```

---

## 🎮 Primeiras Ações

```
✅ Diga: "Olá Otto"
✅ Digite: "Como você funciona?"
✅ Clique no microfone e fale
✅ Veja a orbe 3D se movendo com a fala
✅ Crie seu primeiro projeto
✅ Configure seus lembretes
```

---

## 🐛 Troubleshooting

### App não inicia
- Limpe o cache: `npm start -- --reset-cache`
- Reinstale: `rm -rf node_modules && npm install`

### Voz não funciona
- Verifique permissões de microfone
- Cheque a chave da ElevenLabs

### Firebase não conecta
- Verifique as credenciais no .env
- Confirme que o projeto Firebase existe

### Backend não responde
- Verifique se FastAPI está rodando
- Confirme a URL da API no app

---

## 📧 Suporte

Tem dúvidas ou problemas?

📧 **Email:** suporte.dev.victor@gmail.com

---

**Criado por Victor G. © 2024**
