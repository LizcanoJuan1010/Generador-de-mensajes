# Templates de cuerpo de mensaje por grupo de edad.
# Placeholders: {nombre}, {propuesta_titulo}, {propuesta_desc}
#
# Cada template NO incluye el saludo inicial ni el cierre con la web/radicado.
# Esos se agregan en message_builder.py.
#
# Tecnicas de copywriting usadas:
#   [P] Pregunta-gancho    [U] Urgencia temporal     [PS] Problema-solucion
#   [SO] Prueba social     [D] Desafio directo       [E] Emocional/esperanza
#   [I] Interactivo        [DI] Dato impactante

TEMPLATES = {
    "18-25": [
        # [P] Pregunta-gancho
        (
            "{nombre}, sabias que Horacio Jose Serpa propone {propuesta_desc}? "
            "Tu voz importa, se parte del cambio!"
        ),
        # [E] Emocional/esperanza
        (
            "{nombre}, imagina un futuro con {propuesta_desc}. "
            "Horacio Jose Serpa trabaja por los jovenes como tu. Informate y actua!"
        ),
        # [D] Desafio directo
        (
            "{nombre}, el cambio depende de ti. Horacio Jose Serpa propone "
            "{propuesta_desc}. Tu decides si Colombia avanza o se queda igual."
        ),
        # [U] Urgencia temporal
        (
            "{nombre}, el 8 de marzo se decide tu futuro. Horacio Jose Serpa propone "
            "{propuesta_titulo}: {propuesta_desc}. No te quedes sin saber."
        ),
        # [SO] Prueba social
        (
            "{nombre}, miles de jovenes en Colombia ya apoyan la propuesta de {propuesta_titulo}. "
            "Se trata de {propuesta_desc}. Sumate!"
        ),
        # [PS] Problema-solucion
        (
            "{nombre}, cansado de promesas vacias? Horacio Jose Serpa tiene una propuesta concreta: "
            "{propuesta_desc}. Esto si es real."
        ),
        # [I] Interactivo
        (
            "{nombre}, que opinas de esto: {propuesta_desc}? "
            "Esa es la propuesta de {propuesta_titulo} de Horacio Jose Serpa. Tu que piensas?"
        ),
        # [DI] Dato impactante
        (
            "{nombre}, en Colombia necesitamos cambios reales. Horacio Jose Serpa propone "
            "{propuesta_desc}. Es hora de actuar, no solo de hablar."
        ),
        # Variante energetica
        (
            "{nombre}, esto te va a interesar: {propuesta_titulo}. Horacio Jose Serpa quiere "
            "{propuesta_desc}. Es por los jovenes como tu!"
        ),
        # Variante directa
        (
            "{nombre}, si pudieras cambiar algo en Colombia, que seria? Horacio Jose Serpa ya "
            "tiene plan: {propuesta_desc}. Conocelo."
        ),
    ],
    "26-35": [
        # [P] Pregunta-gancho
        (
            "{nombre}, te has preguntado como seria un pais con {propuesta_desc}? "
            "Horacio Jose Serpa tiene un plan concreto. Conocelo."
        ),
        # [E] Emocional/esperanza
        (
            "{nombre}, Horacio Jose Serpa tiene una propuesta que puede impactar tu vida: "
            "{propuesta_desc}. Conoce su plan completo para el Senado."
        ),
        # [D] Desafio directo
        (
            "{nombre}, tu generacion esta construyendo el futuro del pais. Horacio Jose Serpa propone "
            "{propuesta_desc}. Informate y decide con criterio."
        ),
        # [U] Urgencia temporal
        (
            "{nombre}, el 8 de marzo se eligen los senadores que definiran tu futuro. "
            "Horacio Jose Serpa propone {propuesta_titulo}: {propuesta_desc}."
        ),
        # [SO] Prueba social
        (
            "{nombre}, profesionales de todo el pais ya estan conociendo la propuesta de "
            "{propuesta_titulo}: {propuesta_desc}. Tu tambien mereces estar informado."
        ),
        # [PS] Problema-solucion
        (
            "{nombre}, sabemos que hay problemas serios en Colombia. Horacio Jose Serpa no promete "
            "magia, propone soluciones reales: {propuesta_desc}."
        ),
        # [I] Interactivo
        (
            "{nombre}, la propuesta de {propuesta_titulo} busca {propuesta_desc}. "
            "Que impacto crees que tendria en tu vida? Horacio Jose Serpa quiere escucharte."
        ),
        # [DI] Dato impactante
        (
            "{nombre}, Colombia necesita senadores con propuestas concretas. "
            "Horacio Jose Serpa propone {propuesta_desc}. Eso es gobernar con ideas, no con discursos."
        ),
        # Variante motivadora
        (
            "{nombre}, tu capacidad para transformar a Colombia es real. Horacio Jose Serpa "
            "cree en esta generacion y propone {propuesta_desc}."
        ),
    ],
    "36-50": [
        # [P] Pregunta-gancho
        (
            "{nombre}, se ha preguntado que pasaria si en Colombia se lograra {propuesta_desc}? "
            "Horacio Jose Serpa trabaja para hacerlo realidad."
        ),
        # [E] Emocional/esperanza
        (
            "{nombre}, como persona comprometida con su familia, le invitamos a conocer "
            "la propuesta de Horacio Jose Serpa: {propuesta_titulo} — {propuesta_desc}."
        ),
        # [D] Desafio directo
        (
            "{nombre}, usted tiene el poder de decidir que pais le deja a sus hijos. "
            "Horacio Jose Serpa propone {propuesta_desc}. Informese y decida."
        ),
        # [U] Urgencia temporal
        (
            "{nombre}, el 8 de marzo su voto define el rumbo del pais. Horacio Jose Serpa "
            "propone {propuesta_titulo}: {propuesta_desc}."
        ),
        # [SO] Prueba social
        (
            "{nombre}, familias de todo el pais ya conocen la propuesta de {propuesta_titulo}: "
            "{propuesta_desc}. Su familia tambien merece esta informacion."
        ),
        # [PS] Problema-solucion
        (
            "{nombre}, Horacio Jose Serpa sabe que usted trabaja por el bienestar de los suyos. "
            "Por eso propone {propuesta_desc}. Soluciones reales para familias reales."
        ),
        # [I] Interactivo
        (
            "{nombre}, la propuesta {propuesta_titulo} busca {propuesta_desc}. "
            "Como cree que beneficiaria a su comunidad? Horacio Jose Serpa quiere saberlo."
        ),
        # [DI] Dato impactante
        (
            "{nombre}, su experiencia y compromiso son valiosos. Horacio Jose Serpa propone "
            "{propuesta_desc}. Un Senado con propuestas concretas es posible."
        ),
        # Variante familiar
        (
            "{nombre}, por el futuro de su familia y su comunidad, conozca la propuesta de "
            "Horacio Jose Serpa sobre {propuesta_titulo}: {propuesta_desc}."
        ),
    ],
    "51+": [
        # [P] Pregunta-gancho
        (
            "{nombre}, alguna vez imagino un Senado que realmente trabajara por usted? "
            "Horacio Jose Serpa propone {propuesta_titulo}: {propuesta_desc}."
        ),
        # [E] Emocional/esperanza
        (
            "{nombre}, usted que ha dado tanto por este pais merece un Senado que lo represente. "
            "Horacio Jose Serpa propone {propuesta_desc}. Cuente con el."
        ),
        # [D] Desafio directo
        (
            "{nombre}, con todo respeto le invitamos a conocer la propuesta de Horacio Jose Serpa "
            "sobre {propuesta_titulo}: {propuesta_desc}. Su voto y su experiencia son fundamentales."
        ),
        # [U] Urgencia temporal
        (
            "{nombre}, el 8 de marzo Colombia elige su futuro. Horacio Jose Serpa propone "
            "{propuesta_titulo}: {propuesta_desc}. Su voto cuenta."
        ),
        # [SO] Prueba social
        (
            "{nombre}, colombianos de todas las regiones ya confian en la propuesta de "
            "{propuesta_titulo}: {propuesta_desc}. Conozca por que."
        ),
        # [PS] Problema-solucion
        (
            "{nombre}, Horacio Jose Serpa valora su trayectoria. Por eso propone {propuesta_desc}. "
            "No son promesas, son proyectos de ley concretos."
        ),
        # [I] Interactivo
        (
            "{nombre}, la propuesta de {propuesta_titulo} de Horacio Jose Serpa busca "
            "{propuesta_desc}. Que le parece? Su opinion es muy importante."
        ),
        # [DI] Dato impactante
        (
            "{nombre}, su sabiduria y experiencia son el motor del cambio que Colombia necesita. "
            "Horacio Jose Serpa propone {propuesta_desc}. Hagamoslo juntos."
        ),
        # Variante legado
        (
            "{nombre}, por el pais que queremos dejarle a las nuevas generaciones, "
            "Horacio Jose Serpa propone {propuesta_titulo}: {propuesta_desc}."
        ),
    ],
}

# Propuestas prioritarias por grupo de edad (claves de proposals.py)
AGE_GROUP_PROPOSAL_PRIORITIES = {
    "18-25": [
        "icetex_justo",
        "productividad_turismo",
        "violadores_no_mas",
    ],
    "26-35": [
        "icetex_justo",
        "no_valorizaciones",
        "productividad_turismo",
        "comida_no_se_bota",
    ],
    "36-50": [
        "pension_parejas",
        "comida_no_se_bota",
        "limites_presidente",
        "rio_magdalena",
    ],
    "51+": [
        "pension_parejas",
        "seguridad_libertad",
        "comida_no_se_bota",
        "limites_presidente",
    ],
}

# Cierres con invitacion a la web, personalizados por grupo de edad.
# Son LISTAS para mayor variedad (se elige uno al azar).
CLOSINGS = {
    "18-25": [
        "Entra ya a https://www.horacioserpa.com/ y conoce todas las propuestas!",
        "El 8 de marzo decides tu futuro. Informate en https://www.horacioserpa.com/",
        "Si quieres un pais diferente, empieza por informarte: https://www.horacioserpa.com/",
        "Miles de jovenes ya se sumaron. Unete en https://www.horacioserpa.com/",
        "Que propuesta te representa mas? Descubrelo en https://www.horacioserpa.com/",
        "Tu voto es tu poder. Usalo con informacion: https://www.horacioserpa.com/",
    ],
    "26-35": [
        "Conoce el plan completo en https://www.horacioserpa.com/ y decide con criterio.",
        "El 8 de marzo se define el rumbo. Preparate en https://www.horacioserpa.com/",
        "Toma una decision informada. Revisa las propuestas en https://www.horacioserpa.com/",
        "Profesionales como tu ya estan participando. Visita https://www.horacioserpa.com/",
        "Cual propuesta impacta mas tu vida? Exploralas en https://www.horacioserpa.com/",
        "Colombia necesita ciudadanos informados como tu. https://www.horacioserpa.com/",
    ],
    "36-50": [
        "Conozca todas las propuestas en https://www.horacioserpa.com/",
        "El 8 de marzo el futuro de su familia esta en juego. Informese en https://www.horacioserpa.com/",
        "Por el futuro de los suyos, conozca las propuestas en https://www.horacioserpa.com/",
        "Familias de todo el pais ya se estan informando. Visite https://www.horacioserpa.com/",
        "Que propuesta beneficia mas a su familia? Descubralo en https://www.horacioserpa.com/",
        "Un Senado que trabaja por usted. Conozca como en https://www.horacioserpa.com/",
    ],
    "51+": [
        "Le invitamos a conocer las propuestas en https://www.horacioserpa.com/",
        "El 8 de marzo su voto define el futuro de Colombia. Informese en https://www.horacioserpa.com/",
        "Su experiencia merece un Senado a la altura. Conozca las propuestas en https://www.horacioserpa.com/",
        "Colombianos de todo el pais confian en este proyecto. Visite https://www.horacioserpa.com/",
        "Por el pais que queremos dejar a las nuevas generaciones: https://www.horacioserpa.com/",
        "Gracias por su tiempo. Conozca mas en https://www.horacioserpa.com/",
    ],
}
