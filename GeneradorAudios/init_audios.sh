#!/bin/bash
# ============================================
# init_audios.sh
# Levanta el servicio y genera los 30 audios base con ElevenLabs.
# Ejecutar una sola vez en la PC donde se vaya a usar.
#
# Requisitos:
#   - Docker y Docker Compose instalados
#   - Dashboard DB corriendo (docker compose up db -d en Dashboard/)
#   - API key de ElevenLabs con permiso text_to_speech en ../.env
#
# Uso:
#   chmod +x init_audios.sh
#   ./init_audios.sh
# ============================================

set -e

echo "=== GeneradorAudios HJS 2026 ==="
echo ""

# 1. Verificar que el .env existe
if [ ! -f "../.env" ]; then
    echo "ERROR: No se encontro ../.env con ELEVENLABS_API_KEY"
    echo "Crea el archivo con: echo 'ELEVENLABS_API_KEY=tu_key_aqui' > ../.env"
    exit 1
fi

echo "[1/4] Verificando red de Docker del Dashboard..."
if ! docker network ls | grep -q dashboard_default; then
    echo "AVISO: Red 'dashboard_default' no encontrada. Asegurate de que el Dashboard este levantado."
    echo "Ejecuta: cd ../Dashboard && docker compose up db -d"
    exit 1
fi

echo "[2/4] Construyendo y levantando el servicio..."
docker compose up --build -d

echo "[3/4] Esperando a que el servicio arranque..."
for i in $(seq 1 20); do
    if curl -s http://localhost:8007/ > /dev/null 2>&1; then
        echo "       Servicio listo!"
        break
    fi
    echo "       Esperando... ($i/20)"
    sleep 3
done

# Verificar que realmente arranco
if ! curl -s http://localhost:8007/ > /dev/null 2>&1; then
    echo "ERROR: El servicio no arranco. Revisa logs con: docker logs generadoraudios-generador-audios-1"
    exit 1
fi

echo "[4/4] Generando 30 segmentos base con ElevenLabs (esto tarda ~2 min)..."
echo "       (10 intros + 10 cuerpos de campana + 10 cierres)"
echo ""

RESULT=$(curl -s -X POST http://localhost:8007/api/audio/init --max-time 600)

echo "Resultado: $RESULT"
echo ""
echo "=== LISTO ==="
echo ""
echo "Endpoints disponibles:"
echo "  Swagger:          http://localhost:8007/docs"
echo "  Generar audio:    http://localhost:8007/api/audio/generate?nombre=Carlos"
echo "  Descargar MP3:    http://localhost:8007/api/audio/generate?nombre=Carlos&download=true"
echo "  Siguiente en BD:  http://localhost:8007/api/audio/next"
echo "  Stats del cache:  http://localhost:8007/api/audio/cache/stats"
