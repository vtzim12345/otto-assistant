from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from contextlib import asynccontextmanager

from src.config.settings import settings
from src.config.firebase_config import initialize_firebase
from src.api.routes import auth, chat, voice, vision, projects, reminders, settings as settings_routes
from src.core.websocket_manager import ConnectionManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# WebSocket manager
manager = ConnectionManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("🚀 Starting OTTO Backend...")
    initialize_firebase()
    logger.info("✅ Firebase initialized")
    yield
    # Shutdown
    logger.info("🛑 Shutting down OTTO Backend...")

app = FastAPI(
    title="OTTO API",
    description="Intelligent Personal Assistant API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "message": "OTTO is running smoothly 🎯"
    }

# WebSocket Endpoint
@app.websocket("/ws/chat/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_json()
            # Process incoming message
            response = await process_message(data)
            await manager.broadcast(response)
    except WebSocketDisconnect:
        manager.disconnect(client_id)
        logger.info(f"Client {client_id} disconnected")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(voice.router, prefix="/voice", tags=["Voice"])
app.include_router(vision.router, prefix="/vision", tags=["Vision"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(reminders.router, prefix="/reminders", tags=["Reminders"])
app.include_router(settings_routes.router, prefix="/settings", tags=["Settings"])

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "message": str(exc)}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.DEBUG
    )
