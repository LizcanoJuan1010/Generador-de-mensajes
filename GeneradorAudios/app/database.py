import asyncio
import logging
from databases import Database
from app.config import settings

logger = logging.getLogger(__name__)

database = Database(settings.database_url)

CREATE_CACHE_TABLE = """
CREATE TABLE IF NOT EXISTS audio_cache (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(20) NOT NULL,
    clave VARCHAR(255) NOT NULL,
    audio_data BYTEA NOT NULL,
    duracion_ms INTEGER DEFAULT 0,
    voice_id VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(tipo, clave)
);
"""


async def connect_db():
    for attempt in range(10):
        try:
            await database.connect()
            logger.info("Conectado a PostgreSQL")
            await database.execute(query=CREATE_CACHE_TABLE)
            logger.info("Tabla audio_cache verificada/creada")
            return
        except Exception as e:
            logger.warning(f"Intento {attempt + 1}/10 fallido: {e}")
            await asyncio.sleep(3)
    raise RuntimeError("No se pudo conectar a la base de datos despues de 10 intentos")


async def disconnect_db():
    await database.disconnect()
    logger.info("Desconectado de PostgreSQL")
