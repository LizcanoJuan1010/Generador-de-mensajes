import logging
from typing import Optional
from app.database import database

logger = logging.getLogger(__name__)


async def get_cached(tipo: str, clave: str) -> Optional[bytes]:
    """Busca un audio en cache. Retorna bytes o None."""
    row = await database.fetch_one(
        query="SELECT audio_data FROM audio_cache WHERE tipo = :tipo AND clave = :clave",
        values={"tipo": tipo, "clave": clave},
    )
    if row:
        return row["audio_data"]
    return None


async def store_cached(tipo: str, clave: str, audio_data: bytes, duracion_ms: int = 0, voice_id: str = None):
    """Guarda un audio en cache. Si ya existe, lo ignora."""
    await database.execute(
        query="""
            INSERT INTO audio_cache (tipo, clave, audio_data, duracion_ms, voice_id)
            VALUES (:tipo, :clave, :audio_data, :duracion_ms, :voice_id)
            ON CONFLICT (tipo, clave) DO NOTHING
        """,
        values={
            "tipo": tipo,
            "clave": clave,
            "audio_data": audio_data,
            "duracion_ms": duracion_ms,
            "voice_id": voice_id,
        },
    )
    logger.info(f"Cache almacenado: {tipo}/{clave} ({len(audio_data)} bytes)")


async def get_cache_stats() -> dict:
    """Estadisticas del cache de audio."""
    rows = await database.fetch_all(
        query="""
            SELECT
                tipo,
                COUNT(*) as cantidad,
                SUM(LENGTH(audio_data)) as bytes_total
            FROM audio_cache
            GROUP BY tipo
            ORDER BY tipo
        """
    )
    stats = {}
    for row in rows:
        stats[row["tipo"]] = {
            "cantidad": row["cantidad"],
            "bytes_total": row["bytes_total"],
            "mb_total": round(row["bytes_total"] / (1024 * 1024), 2),
        }
    total = await database.fetch_val(query="SELECT COUNT(*) FROM audio_cache")
    return {"total_segmentos": total, "por_tipo": stats}
