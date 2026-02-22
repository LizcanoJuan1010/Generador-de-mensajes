import io
import logging
import httpx
from gtts import gTTS
from app.config import settings

logger = logging.getLogger(__name__)

BASE_URL = "https://api.elevenlabs.io/v1"

VOICE_SETTINGS = {
    "stability": 0.50,
    "similarity_boost": 0.75,
    "style": 0.0,
    "use_speaker_boost": True,
}


def demo_tts(text: str) -> bytes:
    """
    TTS gratuito con Google (gTTS) para modo demo/pruebas.
    Voz femenina espanol-colombiano. Sirve para probar el flujo completo.
    """
    tts = gTTS(text=text, lang="es", tld="com.co", slow=False)
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    buf.seek(0)
    audio_bytes = buf.read()
    logger.info(f"Demo TTS: '{text[:40]}...' ({len(audio_bytes)} bytes)")
    return audio_bytes


async def text_to_speech(text: str, voice_id: str = None, demo: bool = False) -> bytes:
    """
    Genera audio TTS.
    - demo=True: usa gTTS (gratis, para pruebas)
    - demo=False: usa ElevenLabs con la voz de Horacio
    """
    if demo:
        return demo_tts(text)

    vid = voice_id or settings.ELEVENLABS_VOICE_ID
    url = f"{BASE_URL}/text-to-speech/{vid}"

    payload = {
        "text": text,
        "model_id": settings.ELEVENLABS_MODEL,
        "voice_settings": VOICE_SETTINGS,
    }

    headers = {
        "xi-api-key": settings.ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        logger.info(f"ElevenLabs TTS: '{text[:40]}...' ({len(resp.content)} bytes)")
        return resp.content
