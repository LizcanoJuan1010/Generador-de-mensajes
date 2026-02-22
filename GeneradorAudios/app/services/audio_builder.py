import io
import random
import logging
from pydub import AudioSegment

from app.data.scripts import INTRO_SCRIPTS, BODY_SCRIPTS, CLOSING_SCRIPTS
from app.services.elevenlabs_client import text_to_speech
from app.services import audio_cache

logger = logging.getLogger(__name__)

# Silencios entre segmentos (ms) — simulan pausas naturales de un audio de WhatsApp.
# Un audio real tiene pausas de ~0.8-1.2s entre ideas.
PAUSE_AFTER_INTRO = 800      # despues del saludo, antes de decir el nombre
PAUSE_AFTER_NAME_1 = 1000    # despues del nombre, antes del pitch (pausa larga, "pensando")
PAUSE_BEFORE_CLOSE = 900     # despues del pitch, antes del cierre
PAUSE_BEFORE_NAME_2 = 500    # antes del nombre final despues de "chao"

# Fade in/out para que los cortes no suenen bruscos
FADE_MS = 80


def _bytes_to_segment(mp3_bytes: bytes) -> AudioSegment:
    return AudioSegment.from_mp3(io.BytesIO(mp3_bytes))


def _segment_to_bytes(segment: AudioSegment) -> bytes:
    buf = io.BytesIO()
    segment.export(buf, format="mp3", bitrate="128k")
    return buf.getvalue()


def _silence(ms: int) -> AudioSegment:
    return AudioSegment.silent(duration=ms)


def _smooth(seg: AudioSegment) -> AudioSegment:
    """Aplica fade-in y fade-out suave para evitar cortes bruscos."""
    return seg.fade_in(FADE_MS).fade_out(FADE_MS)


async def _get_or_generate(tipo: str, clave: str, text: str, demo: bool = False) -> bytes:
    """
    Busca audio en cache. Si no existe, lo genera y lo guarda.
    demo=True usa gTTS gratis, demo=False usa ElevenLabs.
    """
    # En modo demo usamos claves separadas para no mezclar con produccion
    cache_clave = f"demo_{clave}" if demo else clave

    cached = await audio_cache.get_cached(tipo, cache_clave)
    if cached:
        logger.debug(f"Cache HIT: {tipo}/{cache_clave}")
        return cached

    tts_label = "gTTS demo" if demo else "ElevenLabs"
    logger.info(f"Cache MISS: {tipo}/{cache_clave} -> generando con {tts_label}...")
    audio_bytes = await text_to_speech(text, demo=demo)
    await audio_cache.store_cached(tipo, cache_clave, audio_bytes)
    return audio_bytes


async def init_base_segments(demo: bool = False):
    """
    Pre-genera los 30 segmentos base (10 intros + 10 cuerpos + 10 cierres).
    demo=True usa gTTS para pruebas sin costo.
    """
    generated = 0
    cached = 0

    segments = [
        ("intro", INTRO_SCRIPTS),
        ("cuerpo", BODY_SCRIPTS),
        ("cierre", CLOSING_SCRIPTS),
    ]

    for tipo, scripts in segments:
        for i, text in enumerate(scripts):
            clave = f"demo_{tipo}_{i:02d}" if demo else f"{tipo}_{i:02d}"
            existing = await audio_cache.get_cached(tipo, clave)
            if existing:
                cached += 1
            else:
                audio_bytes = await text_to_speech(text, demo=demo)
                await audio_cache.store_cached(tipo, clave, audio_bytes)
                generated += 1

    return {"generados": generated, "ya_en_cache": cached, "total": generated + cached}


async def build_voice_message(nombre: str, demo: bool = False) -> dict:
    """
    Construye el mensaje de voz completo para una persona.

    Flujo:
      [intro] → 0.8s → [nombre] → 1.0s → [cuerpo campana] → 0.9s → [cierre SERPAIS] → 0.5s → [nombre]

    Cada segmento tiene fade-in/out de 80ms para suavizar los cortes.
    """
    nombre_clean = nombre.strip().title()
    prefix = "demo_" if demo else ""

    # 1. Elegir variantes al azar
    intro_idx = random.randint(0, len(INTRO_SCRIPTS) - 1)
    body_idx = random.randint(0, len(BODY_SCRIPTS) - 1)
    close_idx = random.randint(0, len(CLOSING_SCRIPTS) - 1)

    # 2. Obtener audios (cache o generar)
    intro_bytes = await _get_or_generate("intro", f"{prefix}intro_{intro_idx:02d}", INTRO_SCRIPTS[intro_idx], demo)
    nombre_bytes = await _get_or_generate("nombre", f"{prefix}{nombre_clean.lower()}", nombre_clean, demo)
    body_bytes = await _get_or_generate("cuerpo", f"{prefix}body_{body_idx:02d}", BODY_SCRIPTS[body_idx], demo)
    close_bytes = await _get_or_generate("cierre", f"{prefix}close_{close_idx:02d}", CLOSING_SCRIPTS[close_idx], demo)

    # 3. Convertir a AudioSegment y suavizar bordes
    intro_seg = _smooth(_bytes_to_segment(intro_bytes))
    nombre_seg = _smooth(_bytes_to_segment(nombre_bytes))
    body_seg = _smooth(_bytes_to_segment(body_bytes))
    close_seg = _smooth(_bytes_to_segment(close_bytes))

    # 4. Ensamblar con pausas naturales
    final = (
        intro_seg
        + _silence(PAUSE_AFTER_INTRO)
        + nombre_seg
        + _silence(PAUSE_AFTER_NAME_1)
        + body_seg
        + _silence(PAUSE_BEFORE_CLOSE)
        + close_seg
        + _silence(PAUSE_BEFORE_NAME_2)
        + nombre_seg
    )

    final_bytes = _segment_to_bytes(final)
    duracion_ms = len(final)

    return {
        "audio": final_bytes,
        "duracion_ms": duracion_ms,
        "duracion_seg": round(duracion_ms / 1000, 1),
        "modo": "demo (gTTS)" if demo else "produccion (ElevenLabs)",
        "segmentos": {
            "intro": INTRO_SCRIPTS[intro_idx],
            "nombre": nombre_clean,
            "cuerpo": BODY_SCRIPTS[body_idx][:80] + "...",
            "cierre": CLOSING_SCRIPTS[close_idx][:80] + "...",
        },
        "pausas_ms": {
            "despues_saludo": PAUSE_AFTER_INTRO,
            "despues_nombre": PAUSE_AFTER_NAME_1,
            "antes_cierre": PAUSE_BEFORE_CLOSE,
            "antes_nombre_final": PAUSE_BEFORE_NAME_2,
        },
    }
