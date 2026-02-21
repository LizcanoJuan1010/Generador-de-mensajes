from pydantic import BaseModel
from typing import List, Optional


class MessageItem(BaseModel):
    celular: str
    nombre: str
    grupo_edad: str
    radicado: str
    mensaje: str


class PaginatedResponse(BaseModel):
    total: int
    limit: int
    offset: int
    count: int
    data: List[MessageItem]


class StatsResponse(BaseModel):
    total_con_celular: int
    por_grupo_edad: dict
    por_genero: dict
    por_departamento: dict
    cruce_edad_genero: dict
