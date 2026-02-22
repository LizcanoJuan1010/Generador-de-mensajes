# Guiones de audio para mensajes de voz de Horacio Jose Serpa.
#
# Estructura del audio final:
#   [intro] + [silencio] + [nombre] + [silencio] + [cuerpo] + [silencio] + [cierre] + [nombre]
#
# Cada lista tiene 10 variantes. Se elige una al azar para cada mensaje.

# --- INTRO: Saludo casual como si grabara un audio de WhatsApp ---
INTRO_SCRIPTS = [
    "Hola, como vamos?",
    "Hola compadre, como estas?",
    "Ey, que mas pues?",
    "Hola, como te va?",
    "Buenas, como vas?",
    "Ey, como estas?",
    "Hola, que tal, todo bien?",
    "Buenas buenas, como va todo?",
    "Ey, te hablo un momentico",
    "Hola, mira te cuento",
]

# --- CUERPO: Pitch de campana, natural y conversacional ---
# Horacio habla como en un audio de WhatsApp, no como un discurso.
BODY_SCRIPTS = [
    (
        "mira, te cuento que me estoy lanzando al Senado por el Partido Liberal "
        "con el numero 09, y tengo unas propuestas muy bacanas que quiero que "
        "conozcas, entra a horacioserpa.com y miralas"
    ),
    (
        "oye, te quiero invitar a que conozcas mis propuestas para el Senado, "
        "estoy con el numero 09 por el Partido Liberal, y la verdad tengo ideas "
        "que creo que te van a gustar"
    ),
    (
        "te cuento que estoy haciendo campana al Senado, soy Horacio Jose Serpa, "
        "numero 09 por el Liberal, y quiero que tu seas parte de este proyecto, "
        "mira mis propuestas en horacioserpa.com"
    ),
    (
        "quiero contarte que me lance al Senado con unas propuestas muy concretas, "
        "como un ICETEX justo, pension compartida para parejas, y mucho mas, "
        "entra a horacioserpa.com y conocelas todas"
    ),
    (
        "mira, estoy trabajando en unas propuestas para el Senado que creo que "
        "te van a interesar mucho, soy el numero 09 por el Partido Liberal, "
        "echales un vistazo en horacioserpa.com"
    ),
    (
        "te escribo porque quiero que conozcas lo que estamos proponiendo para "
        "Colombia, tengo propuestas de seguridad, educacion, pensiones y mas, "
        "numero 09 al Senado, miralas en horacioserpa.com"
    ),
    (
        "hermano, te cuento que estamos en campana al Senado y queremos hacer "
        "las cosas diferente, con propuestas reales no promesas vacias, soy el "
        "09 por el Liberal, conoce el plan en horacioserpa.com"
    ),
    (
        "oye, quiero que sepas que me lance al Senado porque creo que Colombia "
        "necesita gente con propuestas claras, estoy con el numero 09, "
        "te invito a verlas en horacioserpa.com"
    ),
    (
        "mira, soy candidato al Senado numero 09 por el Partido Liberal y "
        "tengo unas propuestas que quiero compartirte, desde ICETEX justo "
        "hasta seguridad real, todo esta en horacioserpa.com"
    ),
    (
        "te quiero contar que estamos construyendo un proyecto para el Senado "
        "con propuestas bien pensadas, no mas de lo mismo, numero 09 por el "
        "Liberal, te espero en horacioserpa.com"
    ),
]

# --- CIERRE: CTA final con SERPAIS y voto, termina con "chao" ---
# Despues del cierre se concatena el nombre de la persona.
CLOSING_SCRIPTS = [
    (
        "que bacano poder hablarte, recuerda, vamos a SERPAIS, "
        "vota por el 09 en el tarjeton, un abrazo, chao"
    ),
    (
        "bueno, espero contar con tu apoyo, SERPAIS, "
        "numero 09 en el tarjeton, un abrazo, chao"
    ),
    (
        "listo, recuerda que el 8 de marzo es la cita, "
        "numero 09, vamos a SERPAIS, un saludo, chao"
    ),
    (
        "bueno, ahi te dejo esa invitacion, el 8 de marzo "
        "vota por el 09, vamos a SERPAIS, nos vemos, chao"
    ),
    (
        "nada, espero que te animes, recuerda, SERPAIS, "
        "numero 09 al Senado por el Liberal, un abrazo, chao"
    ),
    (
        "bueno, cuento contigo, el 8 de marzo numero 09, "
        "vamos a SERPAIS, un abrazo grande, chao"
    ),
    (
        "listo parcero, recuerda, SERPAIS, 09 en el tarjeton, "
        "vamos con toda, un saludo, chao"
    ),
    (
        "bueno, espero que conozcas las propuestas, el 8 de marzo "
        "vota 09, vamos a SERPAIS, cuídate, chao"
    ),
    (
        "nada, ahi queda la invitacion, SERPAIS, numero 09, "
        "nos vemos el 8 de marzo, un abrazo, chao"
    ),
    (
        "bueno, gracias por escucharme, recuerda, 09 al Senado, "
        "vamos a SERPAIS, un saludo muy grande, chao"
    ),
]
