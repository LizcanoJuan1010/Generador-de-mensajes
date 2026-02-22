import asyncio
from datetime import date, timedelta
from typing import Optional

from fastapi import APIRouter, Query

from app.database import database
from app.models.schemas import MessageItem, PaginatedResponse, StatsResponse, BirthdayItem
from app.services.message_builder import (
    generate_message,
    generate_message_with_metadata,
    generate_birthday_message,
)
from app.services.query_builder import (
    build_messages_query,
    build_stats_query,
    build_gender_stats_query,
    build_region_stats_query,
    build_cross_stats_query,
    build_birthday_query,
    build_birthday_count_query,
    build_birthday_stats_query,
)

router = APIRouter()

# --- Estado del cursor en memoria ---
_cursor_state = {"offset": 0, "total": None}

CURSOR_QUERY = """
    SELECT
        empleado_id, celular,
        primer_nombre, segundo_nombre,
        sexo, fecha_nacimiento
    FROM empleados_empresas
    WHERE celular IS NOT NULL AND celular != ''
      AND fecha_nacimiento IS NOT NULL
    ORDER BY empleado_id ASC
    LIMIT 1 OFFSET :offset
"""

CURSOR_COUNT_QUERY = """
    SELECT COUNT(*) FROM empleados_empresas
    WHERE celular IS NOT NULL AND celular != ''
      AND fecha_nacimiento IS NOT NULL
"""


# =============================================
# CURSOR: Recorre registro a registro sin args
# =============================================

@router.get("/next", tags=["Cursor"])
async def next_record():
    """
    Devuelve el SIGUIENTE registro de la base de datos.
    No requiere argumentos. Cada llamada avanza al proximo registro.

    Retorna:
    - **celular**: numero de telefono
    - **mensaje**: mensaje generado personalizado
    - **radicado**: numero de radicado unico
    - **metadata**: info resumida (nombre, edad, grupo, sexo, propuesta, progreso)
    """
    # Obtener total si no lo tenemos aun
    if _cursor_state["total"] is None:
        _cursor_state["total"] = await database.fetch_val(query=CURSOR_COUNT_QUERY)

    total = _cursor_state["total"]
    offset = _cursor_state["offset"]

    # Si ya recorrimos todos los registros
    if offset >= total:
        return {
            "status": "completado",
            "mensaje": f"Se recorrieron los {total} registros. Usa GET /api/cursor/reset para reiniciar.",
            "total_recorridos": total,
            "posicion_actual": offset,
        }

    # Obtener el registro actual
    row = await database.fetch_one(query=CURSOR_QUERY, values={"offset": offset})

    if row is None:
        return {
            "status": "sin_registro",
            "posicion_actual": offset,
            "total": total,
        }

    # Generar mensaje con metadata
    result = generate_message_with_metadata(
        primer_nombre=row["primer_nombre"],
        segundo_nombre=row["segundo_nombre"],
        fecha_nacimiento=row["fecha_nacimiento"],
        sexo=row["sexo"],
    )

    # Avanzar cursor
    _cursor_state["offset"] = offset + 1

    return {
        "celular": row["celular"],
        "mensaje": result["mensaje"],
        "radicado": result["radicado"],
        "metadata": {
            "nombre": result["nombre_generado"],
            "edad": result["edad"],
            "grupo_edad": result["grupo_edad"],
            "sexo": result["sexo"],
            "propuesta": result["propuesta"],
            "posicion": _cursor_state["offset"],
            "total": total,
            "progreso_pct": round((_cursor_state["offset"] / total) * 100, 4),
        },
    }


@router.get("/cursor/reset", tags=["Cursor"])
async def reset_cursor():
    """
    Reinicia el cursor al inicio (registro 0).
    """
    _cursor_state["offset"] = 0
    _cursor_state["total"] = None
    return {"status": "reiniciado", "posicion_actual": 0}


@router.get("/cursor/status", tags=["Cursor"])
async def cursor_status():
    """
    Muestra el estado actual del cursor sin avanzar.
    """
    if _cursor_state["total"] is None:
        _cursor_state["total"] = await database.fetch_val(query=CURSOR_COUNT_QUERY)

    total = _cursor_state["total"]
    offset = _cursor_state["offset"]
    return {
        "posicion_actual": offset,
        "total_registros": total,
        "registros_restantes": total - offset,
        "progreso_pct": round((offset / total) * 100, 4) if total > 0 else 0,
        "completado": offset >= total,
    }


# =============================================
# ENDPOINTS CON FILTROS (existentes)
# =============================================

@router.get("/messages", response_model=PaginatedResponse, tags=["Mensajes"])
async def get_messages(
    cod_departamento: Optional[str] = Query(None, description="Filtrar por codigo de departamento"),
    cod_municipio: Optional[str] = Query(None, description="Filtrar por codigo de municipio"),
    edad_min: Optional[int] = Query(None, ge=18, description="Edad minima"),
    edad_max: Optional[int] = Query(None, le=120, description="Edad maxima"),
    limit: int = Query(50, ge=1, le=500, description="Tamaño de página"),
    offset: int = Query(0, ge=0, description="Desplazamiento de pagina"),
):
    """
    Genera mensajes personalizados de campana con celular y radicado unico.
    Los mensajes se personalizan por grupo de edad y genero.
    """
    data_query, count_query, params = build_messages_query(
        cod_departamento=cod_departamento,
        cod_municipio=cod_municipio,
        edad_min=edad_min,
        edad_max=edad_max,
        limit=limit,
        offset=offset,
    )

    # COUNT y SELECT en paralelo
    count_params = {k: v for k, v in params.items() if k not in ("limit", "offset")}
    total, rows = await asyncio.gather(
        database.fetch_val(query=count_query, values=count_params),
        database.fetch_all(query=data_query, values=params),
    )

    items = []
    for row in rows:
        nombre, group_label, radicado, message = generate_message(
            primer_nombre=row["primer_nombre"],
            segundo_nombre=row["segundo_nombre"],
            fecha_nacimiento=row["fecha_nacimiento"],
            sexo=row["sexo"],
        )
        items.append(
            MessageItem(
                celular=row["celular"],
                nombre=nombre,
                grupo_edad=group_label,
                radicado=radicado,
                mensaje=message,
            )
        )

    return PaginatedResponse(
        total=total,
        limit=limit,
        offset=offset,
        count=len(items),
        data=items,
    )


@router.get("/messages/stats", response_model=StatsResponse, tags=["Estadisticas"])
async def get_message_stats(
    cod_departamento: Optional[str] = Query(None, description="Filtrar por codigo de departamento"),
):
    """
    Estadisticas completas de contactos disponibles:
    - Total con celular
    - Desglose por grupo de edad
    - Desglose por genero
    - Desglose por departamento (top 20)
    - Cruce grupo de edad x genero
    """
    total_where = (
        "WHERE celular IS NOT NULL AND celular != '' "
        "AND fecha_nacimiento IS NOT NULL"
    )
    total_params = {}
    if cod_departamento:
        total_where += " AND cod_departamento = :cod_departamento"
        total_params["cod_departamento"] = cod_departamento

    total_query = f"SELECT COUNT(*) FROM empleados_empresas {total_where}"

    # Construir todas las queries
    age_query, age_params = build_stats_query(cod_departamento)
    gender_query, gender_params = build_gender_stats_query(cod_departamento)
    region_query, region_params = build_region_stats_query(cod_departamento)
    cross_query, cross_params = build_cross_stats_query(cod_departamento)

    # Ejecutar las 5 queries en paralelo
    total, age_rows, gender_rows, region_rows, cross_rows = await asyncio.gather(
        database.fetch_val(query=total_query, values=total_params),
        database.fetch_all(query=age_query, values=age_params),
        database.fetch_all(query=gender_query, values=gender_params),
        database.fetch_all(query=region_query, values=region_params),
        database.fetch_all(query=cross_query, values=cross_params),
    )

    por_grupo = {row["grupo_edad"]: row["total"] for row in age_rows}
    por_genero = {row["genero"]: row["total"] for row in gender_rows}
    por_departamento = {row["cod_departamento"]: row["total"] for row in region_rows}

    # Cruce edad x genero → {"18-25": {"Masculino": 123, "Femenino": 456}, ...}
    cruce = {}
    for row in cross_rows:
        grupo = row["grupo_edad"]
        genero = row["genero"]
        if grupo not in cruce:
            cruce[grupo] = {}
        cruce[grupo][genero] = row["total"]

    return StatsResponse(
        total_con_celular=total,
        por_grupo_edad=por_grupo,
        por_genero=por_genero,
        por_departamento=por_departamento,
        cruce_edad_genero=cruce,
    )


@router.get("/messages/preview", tags=["Preview"])
async def preview_message(
    edad: int = Query(30, ge=18, le=120, description="Edad para el preview"),
    nombre: str = Query("Maria", description="Nombre para el preview"),
    sexo: str = Query("F", description="Sexo (M/F) para personalizar el mensaje"),
):
    """
    Preview de un mensaje de ejemplo para una edad, nombre y sexo dados.
    No consulta la base de datos.
    """
    fake_dob = date.today() - timedelta(days=edad * 365 + edad // 4)
    _, group_label, radicado, message = generate_message(
        primer_nombre=nombre,
        segundo_nombre=None,
        fecha_nacimiento=fake_dob,
        sexo=sexo,
    )
    return {
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo,
        "grupo_edad": group_label,
        "radicado": radicado,
        "mensaje": message,
    }


# =============================================
# CUMPLEANOS: Cursor de cumpleaneros del dia
# =============================================

_birthday_cursor = {"offset": 0, "total": None, "fecha": None}


def _reset_birthday_if_new_day():
    """Reinicia el cursor automaticamente si cambio el dia."""
    today = str(date.today())
    if _birthday_cursor["fecha"] != today:
        _birthday_cursor["offset"] = 0
        _birthday_cursor["total"] = None
        _birthday_cursor["fecha"] = today


@router.get("/birthdays/next", tags=["Cumpleanos"])
async def next_birthday():
    """
    Devuelve el SIGUIENTE cumpleanero de hoy con mensaje personalizado.
    Cada llamada avanza al proximo registro. Cuando no hay mas,
    indica que hoy no cumple mas gente.

    El cursor se reinicia automaticamente al cambiar de dia.
    """
    _reset_birthday_if_new_day()

    if _birthday_cursor["total"] is None:
        _birthday_cursor["total"] = await database.fetch_val(
            query=build_birthday_count_query()
        )

    total = _birthday_cursor["total"]
    offset = _birthday_cursor["offset"]

    # No hay cumpleaneros hoy
    if total == 0:
        return {
            "status": "sin_cumpleaneros",
            "fecha": str(date.today()),
            "mensaje": "Hoy no cumple años nadie en la base de datos.",
            "total_cumpleaneros": 0,
        }

    # Ya recorrimos todos
    if offset >= total:
        return {
            "status": "completado",
            "fecha": str(date.today()),
            "mensaje": f"Hoy no cumple más gente! Ya se felicitaron los {total} cumpleañeros del día.",
            "total_felicitados": total,
            "posicion_actual": offset,
        }

    # Obtener el registro actual
    row = await database.fetch_one(
        query=build_birthday_query(), values={"offset": offset}
    )

    if row is None:
        return {
            "status": "sin_registro",
            "posicion_actual": offset,
            "total": total,
        }

    # Generar mensaje de cumpleanos personalizado
    result = generate_birthday_message(
        primer_nombre=row["primer_nombre"],
        segundo_nombre=row["segundo_nombre"],
        fecha_nacimiento=row["fecha_nacimiento"],
        sexo=row["sexo"],
    )

    # Avanzar cursor
    _birthday_cursor["offset"] = offset + 1

    return {
        "celular": row["celular"],
        "mensaje": result["mensaje"],
        "radicado": result["radicado"],
        "metadata": {
            "nombre": result["nombre"],
            "edad_cumplida": result["edad_cumplida"],
            "grupo_edad": result["grupo_edad"],
            "sexo": result["sexo"],
            "posicion": _birthday_cursor["offset"],
            "total_cumpleaneros": total,
            "restantes": total - _birthday_cursor["offset"],
            "progreso_pct": round((_birthday_cursor["offset"] / total) * 100, 4),
        },
        "fecha": str(date.today()),
    }


@router.get("/birthdays/reset", tags=["Cumpleanos"])
async def reset_birthday_cursor():
    """Reinicia el cursor de cumpleanos al registro 0."""
    _birthday_cursor["offset"] = 0
    _birthday_cursor["total"] = None
    _birthday_cursor["fecha"] = str(date.today())
    return {"status": "reiniciado", "posicion_actual": 0, "fecha": str(date.today())}


@router.get("/birthdays/status", tags=["Cumpleanos"])
async def birthday_cursor_status():
    """Estado actual del cursor de cumpleanos sin avanzar."""
    _reset_birthday_if_new_day()

    if _birthday_cursor["total"] is None:
        _birthday_cursor["total"] = await database.fetch_val(
            query=build_birthday_count_query()
        )

    total = _birthday_cursor["total"]
    offset = _birthday_cursor["offset"]
    return {
        "fecha": str(date.today()),
        "posicion_actual": offset,
        "total_cumpleaneros": total,
        "restantes": total - offset,
        "progreso_pct": round((offset / total) * 100, 4) if total > 0 else 0,
        "completado": offset >= total,
    }


@router.get("/birthdays/stats", tags=["Cumpleanos"])
async def birthday_stats():
    """
    Estadisticas de cumpleaneros de HOY:
    - Total de cumpleaneros
    - Desglose por grupo de edad y genero
    """
    count_query = build_birthday_count_query()
    stats_query = build_birthday_stats_query()

    total, rows = await asyncio.gather(
        database.fetch_val(query=count_query),
        database.fetch_all(query=stats_query),
    )

    # Cruce edad x genero
    por_grupo = {}
    for row in rows:
        grupo = row["grupo_edad"]
        genero = row["genero"]
        if grupo not in por_grupo:
            por_grupo[grupo] = {}
        por_grupo[grupo][genero] = row["total"]

    return {
        "fecha": str(date.today()),
        "total_cumpleaneros": total,
        "por_grupo_edad_y_genero": por_grupo,
    }


@router.get("/birthdays/preview", tags=["Cumpleanos"])
async def preview_birthday(
    nombre: str = Query("Maria", description="Nombre para el preview"),
    edad: int = Query(30, ge=18, le=120, description="Edad que cumple"),
    sexo: str = Query("F", description="Sexo (M/F)"),
):
    """
    Preview de un mensaje de cumpleanos sin consultar la BD.
    Permite probar la personalizacion por genero y edad.
    """
    fake_dob = date.today().replace(year=date.today().year - edad)
    result = generate_birthday_message(
        primer_nombre=nombre,
        segundo_nombre=None,
        fecha_nacimiento=fake_dob,
        sexo=sexo,
    )
    return {
        "fecha": str(date.today()),
        **result,
    }
