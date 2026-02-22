import asyncio
import databases

from app.config import settings

database = databases.Database(settings.database_url)


async def connect_db():
    for attempt in range(10):
        try:
            await database.connect()
            print("Conexion a base de datos exitosa.")
            return
        except Exception as e:
            print(f"Intento {attempt + 1}/10 de conexion fallido: {e}")
            await asyncio.sleep(3)
    raise RuntimeError("No se pudo conectar a la base de datos despues de 10 intentos.")


async def disconnect_db():
    await database.disconnect()
