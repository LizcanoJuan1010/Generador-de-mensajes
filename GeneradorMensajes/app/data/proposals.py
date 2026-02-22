from dataclasses import dataclass


@dataclass
class Proposal:
    key: str
    title: str
    short_description: str


PROPOSALS = [
    Proposal(
        key="seguridad_libertad",
        title="Sin Seguridad no hay Libertad",
        short_description=(
            "integrar cámaras privadas a la Policía y empresas de seguridad "
            "para reacción inmediata ante la inseguridad"
        ),
    ),
    Proposal(
        key="icetex_justo",
        title="ICETEX Justo y Humano",
        short_description=(
            "un ICETEX con cuotas proporcionales al ingreso: "
            "solo pagas cuando trabajas, sin empleo no hay pago"
        ),
    ),
    Proposal(
        key="no_valorizaciones",
        title="No más Valorizaciones Anticipadas",
        short_description=(
            "que solo se pague obra terminada, obra pagada. "
            "Basta de exigir recursos para proyectos que nunca se ejecutan"
        ),
    ),
    Proposal(
        key="comida_no_se_bota",
        title="La Comida no se Bota",
        short_description=(
            "eliminar regulaciones que obligan a desperdiciar alimentos aptos "
            "y conectarlos con bancos de alimentos para quienes los necesitan"
        ),
    ),
    Proposal(
        key="pension_parejas",
        title="Pensión Compartida para Parejas",
        short_description=(
            "permitir ceder semanas de cotización entre la pareja "
            "para que uno de los dos alcance la pensión"
        ),
    ),
    Proposal(
        key="rio_magdalena",
        title="Río Magdalena: Despertar al Gigante",
        short_description=(
            "convertir el Río Magdalena en un eje turístico y de transporte "
            "con infraestructura moderna, impulsando la productividad"
        ),
    ),
    Proposal(
        key="violadores_no_mas",
        title="Violadores, No Más",
        short_description=(
            "un registro permanente e inhabilidad total para agresores sexuales. "
            "Protección real y sin concesiones para nuestras niñas y mujeres"
        ),
    ),
    Proposal(
        key="limites_presidente",
        title="Límites Reales al Presidente",
        short_description=(
            "más autonomía para las regiones y menos centralismo. "
            "Fortalecer las instituciones y el equilibrio democrático"
        ),
    ),
    Proposal(
        key="productividad_turismo",
        title="Productividad, Turismo y Empleo",
        short_description=(
            "IVA cero en vuelos nacionales y estímulos a hotelería "
            "y restaurantes para generar empleo inmediato"
        ),
    ),
]

PROPOSAL_MAP = {p.key: p for p in PROPOSALS}
