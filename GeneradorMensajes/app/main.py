from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import connect_db, disconnect_db
from app.routes.messages import router as messages_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()


app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description="Generador de mensajes personalizados para la campana al Senado de Horacio Jose Serpa 2026",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(messages_router, prefix="/api")


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "GeneradorMensajes",
        "version": settings.APP_VERSION,
        "candidato": "Horacio Jose Serpa - Senado 2026",
    }
