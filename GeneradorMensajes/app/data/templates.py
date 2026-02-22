# Templates de cuerpo de mensaje por grupo de edad.
# Placeholders: {nombre}, {propuesta_titulo}, {propuesta_desc}
#
# Cada template NO incluye el saludo inicial ni el cierre con la web/radicado.
# Esos se agregan en message_builder.py.
#
# Técnicas de copywriting usadas:
#   [P] Pregunta-gancho    [U] Urgencia temporal     [PS] Problema-solución
#   [SO] Prueba social     [D] Desafío directo       [E] Emocional/esperanza
#   [I] Interactivo        [DI] Dato impactante

TEMPLATES = {
    "18-25": [
        # [P] Pregunta-gancho
        (
            "{nombre}, sabías que Horacio José Serpa propone {propuesta_desc}? "
            "Tu voz importa, sé parte del cambio!"
        ),
        # [E] Emocional/esperanza
        (
            "{nombre}, imagina un futuro con {propuesta_desc}. "
            "Horacio José Serpa trabaja por los jóvenes como tú. Infórmate y actúa!"
        ),
        # [D] Desafío directo
        (
            "{nombre}, el cambio depende de ti. Horacio José Serpa propone "
            "{propuesta_desc}. Tú decides si Colombia avanza o se queda igual."
        ),
        # [U] Urgencia temporal
        (
            "{nombre}, el 8 de marzo se decide tu futuro. Horacio José Serpa propone "
            "{propuesta_titulo}: {propuesta_desc}. No te quedes sin saber."
        ),
        # [SO] Prueba social
        (
            "{nombre}, miles de jóvenes en Colombia ya apoyan la propuesta de {propuesta_titulo}. "
            "Se trata de {propuesta_desc}. Súmate!"
        ),
        # [PS] Problema-solución
        (
            "{nombre}, cansado de promesas vacías? Horacio José Serpa tiene una propuesta concreta: "
            "{propuesta_desc}. Esto sí es real."
        ),
        # [I] Interactivo
        (
            "{nombre}, qué opinas de esto: {propuesta_desc}? "
            "Esa es la propuesta de {propuesta_titulo} de Horacio José Serpa. Tú qué piensas?"
        ),
        # [DI] Dato impactante
        (
            "{nombre}, en Colombia necesitamos cambios reales. Horacio José Serpa propone "
            "{propuesta_desc}. Es hora de actuar, no solo de hablar."
        ),
        # Variante energética
        (
            "{nombre}, esto te va a interesar: {propuesta_titulo}. Horacio José Serpa quiere "
            "{propuesta_desc}. Es por los jóvenes como tú!"
        ),
        # Variante directa
        (
            "{nombre}, si pudieras cambiar algo en Colombia, qué sería? Horacio José Serpa ya "
            "tiene plan: {propuesta_desc}. Conócelo."
        ),
    ],
    "26-35": [
        # [P] Pregunta-gancho
        (
            "{nombre}, te has preguntado cómo sería un país con {propuesta_desc}? "
            "Horacio José Serpa tiene un plan concreto. Conócelo."
        ),
        # [E] Emocional/esperanza
        (
            "{nombre}, Horacio José Serpa tiene una propuesta que puede impactar tu vida: "
            "{propuesta_desc}. Conoce su plan completo para el Senado."
        ),
        # [D] Desafío directo
        (
            "{nombre}, tu generación está construyendo el futuro del país. Horacio José Serpa propone "
            "{propuesta_desc}. Infórmate y decide con criterio."
        ),
        # [U] Urgencia temporal
        (
            "{nombre}, el 8 de marzo se eligen los senadores que definirán tu futuro. "
            "Horacio José Serpa propone {propuesta_titulo}: {propuesta_desc}."
        ),
        # [SO] Prueba social
        (
            "{nombre}, profesionales de todo el país ya están conociendo la propuesta de "
            "{propuesta_titulo}: {propuesta_desc}. Tú también mereces estar informado."
        ),
        # [PS] Problema-solución
        (
            "{nombre}, sabemos que hay problemas serios en Colombia. Horacio José Serpa no promete "
            "magia, propone soluciones reales: {propuesta_desc}."
        ),
        # [I] Interactivo
        (
            "{nombre}, la propuesta de {propuesta_titulo} busca {propuesta_desc}. "
            "Qué impacto crees que tendría en tu vida? Horacio José Serpa quiere escucharte."
        ),
        # [DI] Dato impactante
        (
            "{nombre}, Colombia necesita senadores con propuestas concretas. "
            "Horacio José Serpa propone {propuesta_desc}. Eso es gobernar con ideas, no con discursos."
        ),
        # Variante motivadora
        (
            "{nombre}, tu capacidad para transformar a Colombia es real. Horacio José Serpa "
            "cree en esta generación y propone {propuesta_desc}."
        ),
    ],
    "36-50": [
        # [P] Pregunta-gancho
        (
            "{nombre}, se ha preguntado qué pasaría si en Colombia se lograra {propuesta_desc}? "
            "Horacio José Serpa trabaja para hacerlo realidad."
        ),
        # [E] Emocional/esperanza
        (
            "{nombre}, como persona comprometida con su familia, le invitamos a conocer "
            "la propuesta de Horacio José Serpa: {propuesta_titulo} — {propuesta_desc}."
        ),
        # [D] Desafío directo
        (
            "{nombre}, usted tiene el poder de decidir qué país le deja a sus hijos. "
            "Horacio José Serpa propone {propuesta_desc}. Infórmese y decida."
        ),
        # [U] Urgencia temporal
        (
            "{nombre}, el 8 de marzo su voto define el rumbo del país. Horacio José Serpa "
            "propone {propuesta_titulo}: {propuesta_desc}."
        ),
        # [SO] Prueba social
        (
            "{nombre}, familias de todo el país ya conocen la propuesta de {propuesta_titulo}: "
            "{propuesta_desc}. Su familia también merece esta información."
        ),
        # [PS] Problema-solución
        (
            "{nombre}, Horacio José Serpa sabe que usted trabaja por el bienestar de los suyos. "
            "Por eso propone {propuesta_desc}. Soluciones reales para familias reales."
        ),
        # [I] Interactivo
        (
            "{nombre}, la propuesta {propuesta_titulo} busca {propuesta_desc}. "
            "Cómo cree que beneficiaría a su comunidad? Horacio José Serpa quiere saberlo."
        ),
        # [DI] Dato impactante
        (
            "{nombre}, su experiencia y compromiso son valiosos. Horacio José Serpa propone "
            "{propuesta_desc}. Un Senado con propuestas concretas es posible."
        ),
        # Variante familiar
        (
            "{nombre}, por el futuro de su familia y su comunidad, conozca la propuesta de "
            "Horacio José Serpa sobre {propuesta_titulo}: {propuesta_desc}."
        ),
    ],
    "51+": [
        # [P] Pregunta-gancho
        (
            "{nombre}, alguna vez imaginó un Senado que realmente trabajara por usted? "
            "Horacio José Serpa propone {propuesta_titulo}: {propuesta_desc}."
        ),
        # [E] Emocional/esperanza
        (
            "{nombre}, usted que ha dado tanto por este país merece un Senado que lo represente. "
            "Horacio José Serpa propone {propuesta_desc}. Cuente con él."
        ),
        # [D] Desafío directo
        (
            "{nombre}, con todo respeto le invitamos a conocer la propuesta de Horacio José Serpa "
            "sobre {propuesta_titulo}: {propuesta_desc}. Su voto y su experiencia son fundamentales."
        ),
        # [U] Urgencia temporal
        (
            "{nombre}, el 8 de marzo Colombia elige su futuro. Horacio José Serpa propone "
            "{propuesta_titulo}: {propuesta_desc}. Su voto cuenta."
        ),
        # [SO] Prueba social
        (
            "{nombre}, colombianos de todas las regiones ya confían en la propuesta de "
            "{propuesta_titulo}: {propuesta_desc}. Conozca por qué."
        ),
        # [PS] Problema-solución
        (
            "{nombre}, Horacio José Serpa valora su trayectoria. Por eso propone {propuesta_desc}. "
            "No son promesas, son proyectos de ley concretos."
        ),
        # [I] Interactivo
        (
            "{nombre}, la propuesta de {propuesta_titulo} de Horacio José Serpa busca "
            "{propuesta_desc}. Qué le parece? Su opinión es muy importante."
        ),
        # [DI] Dato impactante
        (
            "{nombre}, su sabiduría y experiencia son el motor del cambio que Colombia necesita. "
            "Horacio José Serpa propone {propuesta_desc}. Hagámoslo juntos."
        ),
        # Variante legado
        (
            "{nombre}, por el país que queremos dejarle a las nuevas generaciones, "
            "Horacio José Serpa propone {propuesta_titulo}: {propuesta_desc}."
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

# Cierres con invitación a la web, personalizados por grupo de edad.
# Son LISTAS para mayor variedad (se elige uno al azar).
CLOSINGS = {
    "18-25": [
        "Entra ya a https://www.horacioserpa.com/ y conoce todas las propuestas!",
        "El 8 de marzo decides tu futuro. Infórmate en https://www.horacioserpa.com/",
        "Si quieres un país diferente, empieza por informarte: https://www.horacioserpa.com/",
        "Miles de jóvenes ya se sumaron. Únete en https://www.horacioserpa.com/",
        "Qué propuesta te representa más? Descúbrelo en https://www.horacioserpa.com/",
        "Tu voto es tu poder. Úsalo con información: https://www.horacioserpa.com/",
    ],
    "26-35": [
        "Conoce el plan completo en https://www.horacioserpa.com/ y decide con criterio.",
        "El 8 de marzo se define el rumbo. Prepárate en https://www.horacioserpa.com/",
        "Toma una decisión informada. Revisa las propuestas en https://www.horacioserpa.com/",
        "Profesionales como tú ya están participando. Visita https://www.horacioserpa.com/",
        "Cuál propuesta impacta más tu vida? Explóralas en https://www.horacioserpa.com/",
        "Colombia necesita ciudadanos informados como tú. https://www.horacioserpa.com/",
    ],
    "36-50": [
        "Conozca todas las propuestas en https://www.horacioserpa.com/",
        "El 8 de marzo el futuro de su familia está en juego. Infórmese en https://www.horacioserpa.com/",
        "Por el futuro de los suyos, conozca las propuestas en https://www.horacioserpa.com/",
        "Familias de todo el país ya se están informando. Visite https://www.horacioserpa.com/",
        "Qué propuesta beneficia más a su familia? Descúbralo en https://www.horacioserpa.com/",
        "Un Senado que trabaja por usted. Conozca cómo en https://www.horacioserpa.com/",
    ],
    "51+": [
        "Le invitamos a conocer las propuestas en https://www.horacioserpa.com/",
        "El 8 de marzo su voto define el futuro de Colombia. Infórmese en https://www.horacioserpa.com/",
        "Su experiencia merece un Senado a la altura. Conozca las propuestas en https://www.horacioserpa.com/",
        "Colombianos de todo el país confían en este proyecto. Visite https://www.horacioserpa.com/",
        "Por el país que queremos dejar a las nuevas generaciones: https://www.horacioserpa.com/",
        "Gracias por su tiempo. Conozca más en https://www.horacioserpa.com/",
    ],
}


# =============================================
# TEMPLATES DE CUMPLEAÑOS
# =============================================
# Solo felicitación genuina + invitación a la página.
# Sin propuestas de campaña. El cumpleaños es 100% para la persona.
# Placeholders: {nombre}, {edad}

BIRTHDAY_TEMPLATES = {
    "18-25": [
        "{nombre}, hoy cumples {edad} y eso se celebra! Horacio José Serpa te desea lo mejor en este día tan especial. Pásala increíble!",
        "Hoy es tu día, {nombre}! {edad} años y toda una vida por delante. Un abrazo enorme de parte de Horacio José Serpa!",
        "{nombre}, {edad} años! Qué día tan bacano para celebrar. Horacio José Serpa te envía las mejores vibras!",
        "Ey {nombre}, hoy son {edad}! Disfruta cada momento de este día. Un saludo con mucho cariño de Horacio José Serpa!",
        "{nombre}, feliz {edad}! Que este nuevo año de vida esté lleno de éxitos y alegrías. Horacio José Serpa te desea lo mejor!",
        "Hoy cumples {edad}, {nombre}, y queremos que este año sea el mejor de tu vida. Un abrazo grande de Horacio José Serpa!",
    ],
    "26-35": [
        "{nombre}, hoy cumples {edad} años y queremos desearte lo mejor. Horacio José Serpa te envía un abrazo y las mejores energías para este nuevo año de vida!",
        "En tu día especial, {nombre}, {edad} años bien vividos! Horacio José Serpa te felicita con todo el cariño. Que este cumpleaños sea el inicio de algo grande!",
        "{nombre}, felices {edad}! Hoy es para celebrar y disfrutar. Horacio José Serpa te desea un día increíble rodeado de los tuyos!",
        "Hoy son {edad}, {nombre}! Que tengas un cumpleaños espectacular. Un saludo muy especial de parte de Horacio José Serpa!",
        "{nombre}, {edad} años de experiencia y futuro. Hoy te deseamos lo mejor desde el corazón. Feliz día de parte de Horacio José Serpa!",
        "Felices {edad}, {nombre}! Queremos que este año sea increíble para ti. Un abrazo con mucho aprecio de Horacio José Serpa!",
    ],
    "36-50": [
        "{nombre}, hoy cumple {edad} años y le deseamos un día muy especial. Horacio José Serpa le envía sus más sinceras felicitaciones!",
        "En el día de su cumpleaños, {nombre}, {edad} años bien cumplidos! Horacio José Serpa le desea muchas bendiciones. Que tenga un día maravilloso!",
        "{nombre}, felices {edad} años! Que este nuevo año de vida le traiga muchas bendiciones. Horacio José Serpa le envía un caluroso abrazo!",
        "Le deseamos un feliz cumpleaños, {nombre}! {edad} años de esfuerzo y dedicación que merecen celebrarse. Disfrute su día en familia!",
        "{nombre}, en sus {edad} años, Horacio José Serpa le envía un saludo lleno de aprecio y le desea lo mejor en este día tan especial. Feliz cumpleaños!",
        "Hoy es su día, {nombre}! {edad} años de vida y mucho por delante. Horacio José Serpa le desea lo mejor. Felicidades!",
    ],
    "51+": [
        "{nombre}, hoy cumple {edad} años y Horacio José Serpa le envía sus más sinceras felicitaciones. Su experiencia y sabiduría son invaluables. Feliz día!",
        "En este día tan importante, {nombre}, {edad} años de sabiduría y experiencia. Horacio José Serpa le honra con sus felicitaciones. Que tenga un día hermoso!",
        "{nombre}, felices {edad} años! Que este nuevo año esté lleno de salud y alegría. Horacio José Serpa le envía un abrazo lleno de respeto y cariño!",
        "Le enviamos un caluroso abrazo de cumpleaños, {nombre}! A sus {edad} años, su vida es una inspiración. Felicidades de parte de Horacio José Serpa!",
        "{nombre}, {edad} años de vida que inspiran. Horacio José Serpa le desea un cumpleaños lleno de bendiciones y alegría!",
        "Qué día tan especial, {nombre}! {edad} años bien vividos. Horacio José Serpa le felicita con todo respeto y admiración. Felicidades!",
    ],
}


# Cierres de cumpleaños. Más celebratorios y suaves que los regulares.
BIRTHDAY_CLOSINGS = {
    "18-25": [
        "Que tu nuevo año sea increíble! Conoce más en https://www.horacioserpa.com/",
        "Pásala brutal hoy! Y si quieres, mira las propuestas en https://www.horacioserpa.com/",
        "Disfruta tu día al máximo! Luego échale un ojo a https://www.horacioserpa.com/",
        "Hoy celebra, mañana construimos! https://www.horacioserpa.com/",
        "Un abrazo enorme y feliz cumple! https://www.horacioserpa.com/",
        "Que vengan muchos años más! Visita https://www.horacioserpa.com/",
    ],
    "26-35": [
        "Que este nuevo año de vida traiga grandes logros! Visita https://www.horacioserpa.com/",
        "Disfruta tu día y cuando quieras, conoce las propuestas en https://www.horacioserpa.com/",
        "Feliz día! Si te interesa, más info en https://www.horacioserpa.com/",
        "Un abrazo grande y feliz cumpleaños! https://www.horacioserpa.com/",
        "Que este año sea el mejor! Conoce más en https://www.horacioserpa.com/",
        "Celebra en grande hoy! https://www.horacioserpa.com/",
    ],
    "36-50": [
        "Le deseamos lo mejor en este nuevo año de vida. Visite https://www.horacioserpa.com/",
        "Que tenga un día maravilloso en familia! Más info en https://www.horacioserpa.com/",
        "Felicidades y un abrazo para usted y los suyos! https://www.horacioserpa.com/",
        "Que este nuevo año le traiga salud y prosperidad! https://www.horacioserpa.com/",
        "Disfrute su día, se lo merece! Visite https://www.horacioserpa.com/",
        "Un caluroso abrazo de cumpleaños! https://www.horacioserpa.com/",
    ],
    "51+": [
        "Le deseamos salud y alegría en este nuevo año. Visite https://www.horacioserpa.com/",
        "Que Dios le bendiga en este día tan especial! https://www.horacioserpa.com/",
        "Un abrazo lleno de cariño y respeto! Visite https://www.horacioserpa.com/",
        "Que este nuevo año de vida esté lleno de bendiciones! https://www.horacioserpa.com/",
        "Felicidades con todo nuestro afecto! https://www.horacioserpa.com/",
        "Gracias por tanto, feliz cumpleaños! https://www.horacioserpa.com/",
    ],
}
