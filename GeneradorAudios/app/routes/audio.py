import logging
from fastapi import APIRouter, Query
from fastapi.responses import Response

from app.database import database
from app.services.audio_builder import build_voice_message, init_base_segments
from app.services.audio_cache import get_cache_stats

logger = logging.getLogger(__name__)

router = APIRouter()

# --- Cursor en memoria ---
_cursor = {"offset": 0, "total": None}

CURSOR_QUERY = """
    SELECT
        empleado_id, celular,
        primer_nombre, segundo_nombre
    FROM empleados_empresas
    WHERE celular IS NOT NULL AND celular != ''
      AND primer_nombre IS NOT NULL AND primer_nombre != ''
    ORDER BY empleado_id ASC
    LIMIT 1 OFFSET :offset
"""

CURSOR_COUNT = """
    SELECT COUNT(*) FROM empleados_empresas
    WHERE celular IS NOT NULL AND celular != ''
      AND primer_nombre IS NOT NULL AND primer_nombre != ''
"""


def _build_name(primer: str, segundo: str = None) -> str:
    parts = []
    if primer and primer.strip():
        parts.append(primer.strip().title())
    if segundo and segundo.strip():
        parts.append(segundo.strip().title())
    return " ".join(parts) if parts else "Amigo"


# =============================================
# INIT: Pre-genera segmentos base
# =============================================

@router.post("/init", tags=["Admin"])
async def init_segments(
    demo: bool = Query(False, description="True = usa gTTS gratis para probar. False = usa ElevenLabs."),
):
    """
    Pre-genera los 30 segmentos base (10 intros + 10 cuerpos + 10 cierres).

    - **demo=true**: Usa Google TTS (gratis) para probar el flujo completo.
    - **demo=false**: Usa ElevenLabs con la voz de Horacio (requiere API key activa).

    Solo genera los segmentos que no esten ya en cache.
    """
    result = await init_base_segments(demo=demo)
    return {
        "status": "ok",
        "modo": "demo (gTTS)" if demo else "produccion (ElevenLabs)",
        "segmentos_generados": result["generados"],
        "segmentos_en_cache": result["ya_en_cache"],
        "total_segmentos": result["total"],
    }


# =============================================
# GENERATE: Audio para un nombre especifico
# =============================================

@router.get("/generate", tags=["Audio"])
async def generate_audio(
    nombre: str = Query("Carlos", description="Nombre de la persona"),
    download: bool = Query(False, description="True para descargar el MP3"),
    demo: bool = Query(False, description="True = gTTS gratis para probar"),
):
    """
    Genera un mensaje de voz completo para el nombre dado.

    - **download=false**: retorna metadata (duracion, segmentos usados, link de descarga)
    - **download=true**: retorna el archivo MP3 directamente
    - **demo=true**: usa gTTS para pruebas sin costo
    """
    result = await build_voice_message(nombre, demo=demo)

    if download:
        return Response(
            content=result["audio"],
            media_type="audio/mpeg",
            headers={
                "Content-Disposition": f'attachment; filename="audio_{nombre.lower().replace(" ", "_")}.mp3"',
            },
        )

    return {
        "nombre": result["segmentos"]["nombre"],
        "modo": result["modo"],
        "duracion_ms": result["duracion_ms"],
        "duracion_seg": result["duracion_seg"],
        "tamano_bytes": len(result["audio"]),
        "tamano_kb": round(len(result["audio"]) / 1024, 1),
        "segmentos_usados": result["segmentos"],
        "pausas_ms": result["pausas_ms"],
        "descarga": f"/api/audio/generate?nombre={nombre}&download=true&demo={str(demo).lower()}",
    }


# =============================================
# CURSOR: Recorre la BD registro a registro
# =============================================

@router.get("/next", tags=["Cursor"])
async def next_audio(
    demo: bool = Query(False, description="True = gTTS gratis para probar"),
):
    """
    Genera el audio para el SIGUIENTE registro de la BD.
    Retorna celular, metadata y link de descarga.
    """
    if _cursor["total"] is None:
        _cursor["total"] = await database.fetch_val(query=CURSOR_COUNT)

    total = _cursor["total"]
    offset = _cursor["offset"]

    if offset >= total:
        return {
            "status": "completado",
            "mensaje": f"Se recorrieron los {total} registros. Usa /api/audio/cursor/reset para reiniciar.",
            "total_recorridos": total,
        }

    row = await database.fetch_one(query=CURSOR_QUERY, values={"offset": offset})
    if row is None:
        return {"status": "sin_registro", "posicion": offset, "total": total}

    nombre = _build_name(row["primer_nombre"], row["segundo_nombre"])
    result = await build_voice_message(nombre, demo=demo)

    _cursor["offset"] = offset + 1

    return {
        "celular": row["celular"],
        "nombre": nombre,
        "modo": result["modo"],
        "duracion_seg": result["duracion_seg"],
        "tamano_kb": round(len(result["audio"]) / 1024, 1),
        "segmentos": result["segmentos"],
        "descarga": f"/api/audio/generate?nombre={nombre}&download=true&demo={str(demo).lower()}",
        "cursor": {
            "posicion": _cursor["offset"],
            "total": total,
            "progreso_pct": round((_cursor["offset"] / total) * 100, 4),
        },
    }


@router.get("/cursor/reset", tags=["Cursor"])
async def reset_cursor():
    """Reinicia el cursor al registro 0."""
    _cursor["offset"] = 0
    _cursor["total"] = None
    return {"status": "reiniciado", "posicion": 0}


@router.get("/cursor/status", tags=["Cursor"])
async def cursor_status():
    """Estado actual del cursor sin avanzar."""
    if _cursor["total"] is None:
        _cursor["total"] = await database.fetch_val(query=CURSOR_COUNT)
    total = _cursor["total"]
    offset = _cursor["offset"]
    return {
        "posicion": offset,
        "total": total,
        "restantes": total - offset,
        "progreso_pct": round((offset / total) * 100, 4) if total > 0 else 0,
        "completado": offset >= total,
    }


# =============================================
# CACHE: Estadisticas
# =============================================

@router.get("/cache/stats", tags=["Cache"])
async def cache_stats():
    """Muestra estadisticas del cache de audio en PostgreSQL."""
    return await get_cache_stats()
