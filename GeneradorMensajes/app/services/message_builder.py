import random
import uuid
from datetime import date
from typing import Optional, Tuple

from app.data.greetings import GREETINGS, BIRTHDAY_GREETINGS
from app.data.templates import (
    TEMPLATES, AGE_GROUP_PROPOSAL_PRIORITIES, CLOSINGS,
    BIRTHDAY_TEMPLATES, BIRTHDAY_CLOSINGS,
)
from app.data.proposals import PROPOSAL_MAP


def calculate_age(fecha_nacimiento: date) -> int:
    today = date.today()
    return today.year - fecha_nacimiento.year - (
        (today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
    )


def get_age_group(age: int) -> str:
    if 18 <= age <= 25:
        return "18-25"
    elif 26 <= age <= 35:
        return "26-35"
    elif 36 <= age <= 50:
        return "36-50"
    elif age > 50:
        return "51+"
    return "18-25"


AGE_GROUP_LABELS = {
    "18-25": "Jovenes (18-25)",
    "26-35": "Adultos jovenes (26-35)",
    "36-50": "Adultos (36-50)",
    "51+": "Mayores (51+)",
}


def get_age_group_label(group_key: str) -> str:
    return AGE_GROUP_LABELS.get(group_key, "Desconocido")


def is_female(sexo: Optional[str]) -> bool:
    """Determina si el sexo corresponde a femenino (F)."""
    if not sexo:
        return False
    return sexo.strip().upper() == "F"


def apply_gender(text: str, sexo: Optional[str]) -> str:
    """
    Resuelve marcadores de genero en el texto.
    Patron: 'o(a)' → 'a' si femenino, 'o' si masculino.
    Patron: '(a)' suelto → 'a' si femenino, '' si masculino.
    """
    female = is_female(sexo)
    if female:
        return text.replace("o(a)", "a").replace("O(a)", "A")
    else:
        return text.replace("(a)", "")


def build_name(
    primer_nombre: Optional[str],
    segundo_nombre: Optional[str],
    sexo: Optional[str] = None,
) -> str:
    parts = []
    if primer_nombre and primer_nombre.strip():
        parts.append(primer_nombre.strip().title())
    if segundo_nombre and segundo_nombre.strip():
        parts.append(segundo_nombre.strip().title())
    if parts:
        return " ".join(parts)
    return "Amiga" if is_female(sexo) else "Amigo"


def generate_radicado() -> str:
    code = uuid.uuid4().hex[:8].upper()
    return f"HJS-2026-{code}"


def get_sexo_label(sexo: Optional[str]) -> str:
    if not sexo:
        return "No registrado"
    s = sexo.strip().upper()
    if s == "F":
        return "Femenino"
    if s == "M":
        return "Masculino"
    return "No registrado"


def generate_message(
    primer_nombre: Optional[str],
    segundo_nombre: Optional[str],
    fecha_nacimiento: date,
    sexo: Optional[str] = None,
) -> Tuple[str, str, str, str]:
    """
    Genera un mensaje personalizado.

    Returns:
        (nombre_display, age_group_label, radicado, full_message)
    """
    age = calculate_age(fecha_nacimiento)
    group_key = get_age_group(age)
    group_label = get_age_group_label(group_key)
    nombre = build_name(primer_nombre, segundo_nombre, sexo)

    # Saludo aleatorio por grupo de edad
    greeting = random.choice(GREETINGS[group_key])

    # Propuesta priorizada para este grupo de edad
    priority_keys = AGE_GROUP_PROPOSAL_PRIORITIES.get(group_key, ["comida_no_se_bota"])
    chosen_key = random.choice(priority_keys)
    proposal = PROPOSAL_MAP[chosen_key]

    # Template aleatorio para este grupo de edad
    template = random.choice(TEMPLATES[group_key])
    body = template.format(
        nombre=nombre,
        propuesta_titulo=proposal.title,
        propuesta_desc=proposal.short_description,
    )

    # Cierre aleatorio por grupo de edad
    closing = random.choice(CLOSINGS[group_key])

    # Radicado unico
    radicado = generate_radicado()

    # Mensaje completo con genero aplicado
    raw_message = f"{greeting}, {body} {closing} Radicado: {radicado}"
    full_message = apply_gender(raw_message, sexo)

    return nombre, group_label, radicado, full_message


def generate_message_with_metadata(
    primer_nombre: Optional[str],
    segundo_nombre: Optional[str],
    fecha_nacimiento: date,
    sexo: Optional[str] = None,
) -> dict:
    """
    Genera un mensaje y devuelve metadata resumida.
    """
    age = calculate_age(fecha_nacimiento)
    group_key = get_age_group(age)
    group_label = get_age_group_label(group_key)
    nombre = build_name(primer_nombre, segundo_nombre, sexo)

    greeting = random.choice(GREETINGS[group_key])

    priority_keys = AGE_GROUP_PROPOSAL_PRIORITIES.get(group_key, ["comida_no_se_bota"])
    chosen_key = random.choice(priority_keys)
    proposal = PROPOSAL_MAP[chosen_key]

    template = random.choice(TEMPLATES[group_key])
    body = template.format(
        nombre=nombre,
        propuesta_titulo=proposal.title,
        propuesta_desc=proposal.short_description,
    )

    closing = random.choice(CLOSINGS[group_key])
    radicado = generate_radicado()
    raw_message = f"{greeting}, {body} {closing} Radicado: {radicado}"
    full_message = apply_gender(raw_message, sexo)

    return {
        "nombre_generado": nombre,
        "edad": age,
        "grupo_edad": group_label,
        "sexo": get_sexo_label(sexo),
        "radicado": radicado,
        "mensaje": full_message,
        "propuesta": proposal.title,
    }


def generate_birthday_message(
    primer_nombre: Optional[str],
    segundo_nombre: Optional[str],
    fecha_nacimiento: date,
    sexo: Optional[str] = None,
) -> dict:
    """
    Genera mensaje de cumpleaños personalizado por edad y género.
    Solo felicitación + invitación a la página. Sin propuestas.
    """
    age = calculate_age(fecha_nacimiento)
    group_key = get_age_group(age)
    group_label = get_age_group_label(group_key)
    nombre = build_name(primer_nombre, segundo_nombre, sexo)

    greeting = random.choice(BIRTHDAY_GREETINGS[group_key])

    template = random.choice(BIRTHDAY_TEMPLATES[group_key])
    body = template.format(nombre=nombre, edad=age)

    closing = random.choice(BIRTHDAY_CLOSINGS[group_key])
    radicado = generate_radicado()

    raw_message = f"{greeting} {body} {closing} Radicado: {radicado}"
    full_message = apply_gender(raw_message, sexo)

    return {
        "nombre": nombre,
        "edad_cumplida": age,
        "grupo_edad": group_label,
        "sexo": get_sexo_label(sexo),
        "radicado": radicado,
        "mensaje": full_message,
    }
