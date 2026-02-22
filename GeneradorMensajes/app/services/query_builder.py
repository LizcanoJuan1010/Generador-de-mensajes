from typing import Optional, Tuple, Dict, Any


def build_messages_query(
    cod_departamento: Optional[str] = None,
    cod_municipio: Optional[str] = None,
    edad_min: Optional[int] = None,
    edad_max: Optional[int] = None,
    limit: int = 50,
    offset: int = 0,
) -> Tuple[str, str, Dict[str, Any]]:
    """
    Construye la query de datos y la query de COUNT.

    Returns:
        (data_query, count_query, params)
    """
    select_sql = """
        SELECT
            celular,
            primer_nombre,
            segundo_nombre,
            fecha_nacimiento,
            sexo
        FROM empleados_empresas
    """

    where_clauses = [
        "celular IS NOT NULL",
        "celular != ''",
        "fecha_nacimiento IS NOT NULL",
    ]
    params: Dict[str, Any] = {}

    if cod_departamento:
        where_clauses.append("cod_departamento = :cod_departamento")
        params["cod_departamento"] = cod_departamento

    if cod_municipio:
        where_clauses.append("cod_municipio = :cod_municipio")
        params["cod_municipio"] = cod_municipio

    if edad_min is not None:
        where_clauses.append(
            "fecha_nacimiento <= CURRENT_DATE - CAST(:edad_min || ' years' AS INTERVAL)"
        )
        params["edad_min"] = str(edad_min)

    if edad_max is not None:
        where_clauses.append(
            "fecha_nacimiento > CURRENT_DATE - CAST(:edad_max_plus || ' years' AS INTERVAL)"
        )
        params["edad_max_plus"] = str(edad_max + 1)

    where_str = " WHERE " + " AND ".join(where_clauses)

    count_query = f"SELECT COUNT(*) FROM empleados_empresas{where_str}"

    data_query = (
        select_sql
        + where_str
        + " ORDER BY primer_nombre ASC"
        + " LIMIT :limit OFFSET :offset"
    )
    params["limit"] = limit
    params["offset"] = offset

    return data_query, count_query, params


def build_stats_query(
    cod_departamento: Optional[str] = None,
) -> Tuple[str, Dict[str, Any]]:
    """
    Construye query de estadisticas por grupo de edad.
    """
    base_where = (
        "WHERE celular IS NOT NULL AND celular != '' "
        "AND fecha_nacimiento IS NOT NULL"
    )
    params: Dict[str, Any] = {}

    if cod_departamento:
        base_where += " AND cod_departamento = :cod_departamento"
        params["cod_departamento"] = cod_departamento

    query = f"""
        SELECT
            CASE
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) BETWEEN 18 AND 25 THEN '18-25'
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) BETWEEN 26 AND 35 THEN '26-35'
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) BETWEEN 36 AND 50 THEN '36-50'
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) > 50 THEN '51+'
                ELSE 'Otro'
            END AS grupo_edad,
            COUNT(*) AS total
        FROM empleados_empresas
        {base_where}
        GROUP BY 1
        ORDER BY 1
    """
    return query, params


def build_gender_stats_query(
    cod_departamento: Optional[str] = None,
) -> Tuple[str, Dict[str, Any]]:
    """Estadisticas por genero."""
    base_where = (
        "WHERE celular IS NOT NULL AND celular != '' "
        "AND fecha_nacimiento IS NOT NULL"
    )
    params: Dict[str, Any] = {}

    if cod_departamento:
        base_where += " AND cod_departamento = :cod_departamento"
        params["cod_departamento"] = cod_departamento

    query = f"""
        SELECT
            CASE
                WHEN sexo = 'F' THEN 'Femenino'
                WHEN sexo = 'M' THEN 'Masculino'
                ELSE 'No registrado'
            END AS genero,
            COUNT(*) AS total
        FROM empleados_empresas
        {base_where}
        GROUP BY 1
        ORDER BY 2 DESC
    """
    return query, params


def build_region_stats_query(
    cod_departamento: Optional[str] = None,
) -> Tuple[str, Dict[str, Any]]:
    """Estadisticas por departamento (top 20)."""
    base_where = (
        "WHERE celular IS NOT NULL AND celular != '' "
        "AND fecha_nacimiento IS NOT NULL"
    )
    params: Dict[str, Any] = {}

    if cod_departamento:
        base_where += " AND cod_departamento = :cod_departamento"
        params["cod_departamento"] = cod_departamento

    query = f"""
        SELECT
            cod_departamento,
            COUNT(*) AS total
        FROM empleados_empresas
        {base_where}
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 20
    """
    return query, params


def build_cross_stats_query(
    cod_departamento: Optional[str] = None,
) -> Tuple[str, Dict[str, Any]]:
    """Estadisticas cruzadas: grupo de edad x genero."""
    base_where = (
        "WHERE celular IS NOT NULL AND celular != '' "
        "AND fecha_nacimiento IS NOT NULL"
    )
    params: Dict[str, Any] = {}

    if cod_departamento:
        base_where += " AND cod_departamento = :cod_departamento"
        params["cod_departamento"] = cod_departamento

    query = f"""
        SELECT
            CASE
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) BETWEEN 18 AND 25 THEN '18-25'
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) BETWEEN 26 AND 35 THEN '26-35'
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) BETWEEN 36 AND 50 THEN '36-50'
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) > 50 THEN '51+'
                ELSE 'Otro'
            END AS grupo_edad,
            CASE
                WHEN sexo = 'F' THEN 'Femenino'
                WHEN sexo = 'M' THEN 'Masculino'
                ELSE 'No registrado'
            END AS genero,
            COUNT(*) AS total
        FROM empleados_empresas
        {base_where}
        GROUP BY 1, 2
        ORDER BY 1, 2
    """
    return query, params


def build_birthday_query() -> str:
    """
    Query para cursor de cumpleaneros de HOY.
    Retorna 1 registro a la vez con LIMIT 1 OFFSET :offset.
    """
    return """
        SELECT
            empleado_id, celular,
            primer_nombre, segundo_nombre,
            sexo, fecha_nacimiento
        FROM empleados_empresas
        WHERE EXTRACT(MONTH FROM fecha_nacimiento) = EXTRACT(MONTH FROM CURRENT_DATE)
          AND EXTRACT(DAY FROM fecha_nacimiento) = EXTRACT(DAY FROM CURRENT_DATE)
          AND celular IS NOT NULL AND celular != ''
          AND fecha_nacimiento IS NOT NULL
        ORDER BY empleado_id ASC
        LIMIT 1 OFFSET :offset
    """


def build_birthday_count_query() -> str:
    """Cuenta total de cumpleaneros de HOY."""
    return """
        SELECT COUNT(*) FROM empleados_empresas
        WHERE EXTRACT(MONTH FROM fecha_nacimiento) = EXTRACT(MONTH FROM CURRENT_DATE)
          AND EXTRACT(DAY FROM fecha_nacimiento) = EXTRACT(DAY FROM CURRENT_DATE)
          AND celular IS NOT NULL AND celular != ''
          AND fecha_nacimiento IS NOT NULL
    """


def build_birthday_stats_query() -> str:
    """Stats de cumpleaneros de hoy por grupo de edad y genero."""
    return """
        SELECT
            CASE
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) BETWEEN 18 AND 25 THEN '18-25'
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) BETWEEN 26 AND 35 THEN '26-35'
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) BETWEEN 36 AND 50 THEN '36-50'
                WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) > 50 THEN '51+'
                ELSE 'Otro'
            END AS grupo_edad,
            CASE
                WHEN sexo = 'F' THEN 'Femenino'
                WHEN sexo = 'M' THEN 'Masculino'
                ELSE 'No registrado'
            END AS genero,
            COUNT(*) AS total
        FROM empleados_empresas
        WHERE EXTRACT(MONTH FROM fecha_nacimiento) = EXTRACT(MONTH FROM CURRENT_DATE)
          AND EXTRACT(DAY FROM fecha_nacimiento) = EXTRACT(DAY FROM CURRENT_DATE)
          AND celular IS NOT NULL AND celular != ''
          AND fecha_nacimiento IS NOT NULL
        GROUP BY 1, 2
        ORDER BY 1, 2
    """
