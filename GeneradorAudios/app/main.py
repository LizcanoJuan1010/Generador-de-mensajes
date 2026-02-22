import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import connect_db, disconnect_db
from app.routes.audio import router as audio_router

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()


app = FastAPI(
    title="GeneradorAudios - HJS 2026",
    description=(
        "Microservicio de generacion de mensajes de voz personalizados "
        "para la campana de Horacio Jose Serpa al Senado. "
        "Usa ElevenLabs TTS con la voz clonada de Horacio."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(audio_router, prefix="/api/audio")


@app.get("/", tags=["Health"])
async def root():
    return {
        "servicio": "GeneradorAudios HJS 2026",
        "estado": "activo",
        "docs": "/docs",
        "endpoints": {
            "init_segmentos": "POST /api/audio/init",
            "generar_audio": "GET /api/audio/generate?nombre=Carlos",
            "siguiente_registro": "GET /api/audio/next",
            "reset_cursor": "GET /api/audio/cursor/reset",
            "estado_cursor": "GET /api/audio/cursor/status",
            "cache_stats": "GET /api/audio/cache/stats",
        },
    }
