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
            "integrar camaras privadas a la Policia y empresas de seguridad "
            "para reaccion inmediata ante la inseguridad"
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
        title="No mas Valorizaciones Anticipadas",
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
        title="Pension Compartida para Parejas",
        short_description=(
            "permitir ceder semanas de cotizacion entre la pareja "
            "para que uno de los dos alcance la pension"
        ),
    ),
    Proposal(
        key="rio_magdalena",
        title="Rio Magdalena: Despertar al Gigante",
        short_description=(
            "convertir el Rio Magdalena en un eje turistico y de transporte "
            "con infraestructura moderna, impulsando la productividad"
        ),
    ),
    Proposal(
        key="violadores_no_mas",
        title="Violadores, No Mas",
        short_description=(
            "un registro permanente e inhabilidad total para agresores sexuales. "
            "Proteccion real y sin concesiones para nuestras ninas y mujeres"
        ),
    ),
    Proposal(
        key="limites_presidente",
        title="Limites Reales al Presidente",
        short_description=(
            "mas autonomia para las regiones y menos centralismo. "
            "Fortalecer las instituciones y el equilibrio democratico"
        ),
    ),
    Proposal(
        key="productividad_turismo",
        title="Productividad, Turismo y Empleo",
        short_description=(
            "IVA cero en vuelos nacionales y estimulos a hoteleria "
            "y restaurantes para generar empleo inmediato"
        ),
    ),
]

PROPOSAL_MAP = {p.key: p for p in PROPOSALS}
