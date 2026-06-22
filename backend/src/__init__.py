import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# CORS
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8081",
    "http://10.0.2.2:8000",
    "*"
]
