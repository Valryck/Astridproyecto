# Coloca el codigo de tu juego en este archivo.

# Declara los personajes usados en el juego:

define a = Character("Astrid", color = "#fc03c6")
define dr = Character("Dr Valentin", color = "#323ca8")
define s = Character("Spark Tycoon", color="#ffd700")
define r = Character("Razor Synapse", color="#ff4500")
define d = Character("Dominus Steel", color="#4682b4")
define x = Character("Xander Shadowborne", color="#800080")
define n = Character("Nebula", color="#00c957") # Animal de compañía de Astrid

# Imagenes
image bg_laboratorio = "laboratorio.jpg"
image bg_distrito1 = "distrito1.jpg"
image bg_distrito2 = "distrito2.jpg"
image bg_distrito3 = "distrito3.jpg"
image bg_combate = "combate.jpg"
image transicion1 = "transicion1.jpg" # Agregada
image transicion2 = "transicion2.jpg" # Agregada
image transicion3 = "transicion3.jpg" # Agregada
image background = "fond rose.jpg"
image astrid = "astrid1"
image nebula = "chat.png"
image Drvalentin = "drvalentin"
image tycoon = "tycoon.png"
image xander = "xander.png"
image dominus = "dominus.png"
image razor = "razor.png"




# El juego comienza aquí.

label start:
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    "Bienvenido en el mundo patriarcal de Astrid..."

    pause .5

    scene background with dissolve
    show astrid at left with dissolve
    show nebula at right with dissolve


    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    a "Érase una vez en un mundo patriarcal, donde las mujeres eran frecuentemente subestimadas y sus voces eran silenciadas."
    n "Miau... ¿Otra vez con esas historias, Astrid?"
    a "Sí, Nebula. Es importante recordar por qué estamos luchando. El patriarcado ha influido en casi todos los aspectos de la sociedad, desde la política hasta el hogar."
    n "Lo sé, lo sé. Pero no olvides que tienes una misión que cumplir hoy."
    a "Desde pequeña, me enseñaron que tenía ciertos roles que cumplir simplemente por ser mujer."
    n "Y tú siempre has desafiado esos roles, ¿verdad?"
    a "Así es, Nebula. Siempre he sentido que estos roles me limitaban y no reflejaban mi verdadero potencial."
    n "Por eso estamos aquí, para cambiar las cosas."

    a "Es importante cuestionar estas normas y trabajar para crear una sociedad más equitativa."
    a "La igualdad de género no solo beneficia a las mujeres, sino a toda la humanidad."
    n "Cada día es una batalla, pero no estás sola en esto."

    a "Debemos educar a las próximas generaciones para que comprendan la importancia del respeto y la igualdad."
    a "Solo así podremos desmantelar el patriarcado y construir un futuro más justo para todos."
    n "Sabes que siempre estaré a tu lado, apoyándote."

    a "El viaje no será fácil, pero sé que vale la pena. Porque cada pequeña acción cuenta en esta gran lucha."
    n "Entonces, ¿cuál es el plan para hoy?"




# CHOICE
menu:
    "quiero ir a jugar":
        # hay que ponerlo indentado

        jump jugar
    "en el laboratorio":
        # hay que ponerlo indentado

        jump laboratorio

    # Finaliza el juego:



# BRANCH JUGAR

label jugar:

    a "Buena idea! Vamos a combatir juntos a Spark Tycoon, Razor Synapse y Dominus Steel en cada distrito para llegar al último combatiente, Xander Shadowborne"
  # Primer combate
    scene black with dissolve
    scene bg_distrito1 with dissolve
    show razor at right with dissolve
    s "Astrid, has llegado lejos, pero tu camino termina aquí."
    show astrid at left with dissolve
    a "Razor Synapse, no subestimes mi determinación. Estoy aquí para ganar"

    scene black with dissolve

    "Después de un intenso combate, Astrid emerge victorioso."

    show bg_distrito1 with dissolve
    show astrid with dissolve

    a "Fue una buena pelea, Razor. Pero tengo que seguir adelante."

    scene black with fade
    "Astrid continúa su viaje hacia el próximo distrito..."


    # Segundo combate
    scene bg_distrito2 with dissolve
    show dominus at right with dissolve
    d "Así que has derrotado a Razor. No esperes que te sea tan fácil conmigo, Astrid."
    show astrid at left
    a "Dominus Steel, tu fuerza es legendaria, pero yo confío en mi estrategia."
    show dominus at right
    d "Tu estrategia no te salvará de mi poder."

    scene black with dissolve

    "Con movimientos calculados y rápidos, Spark Tycoon logra vencer a Dominus Steel."


    scene bg_distrito2 with dissolve
    show astrid with dissolve

    a "Otra victoria. Estoy más cerca de mi objetivo."

    scene black with fade
    "Astrid avanza al siguiente distrito, con la determinación firme..."


    # Tercer combate
    scene bg_distrito3 with dissolve
    show xander at right with dissolve
    x "Veo que has llegado lejos, Astrid. Pero tu viaje termina aquí."
    show astrid at left
    a "Xander Shadowborne, he luchado mucho para llegar hasta aquí. No me detendrás."
    show xander at right
    x "Tu determinación es admirable, pero necesitarás más que eso para derrotarme."

    scene black with dissolve

    "El combate final es feroz, pero Astrid da todo lo que tiene y finalmente derrota a Xander Shadowborne."

    scene black with dissolve
    "Astrid ha superado todos los desafíos y se alza como el campeón definitivo. Pero nuevas aventuras esperan..."

    scene black with dissolve
    return




# BRANCH LABORATORIO


label laboratorio:

    scene bg_laboratorio with dissolve

    show astrid at left with dissolve
    show drvalentin at right with dissolve


    a "Genial, sígueme, te voy a presentar a mi amiga: la doctora Valentín"


    a "Dra. Valentín, parece que los circuitos de la interfaz están sobrecargados. ¿Ve esta fluctuación?"

    dr "Sí, Astrid, es preocupante. No estaba previsto en las simulaciones. Debemos actuar rápidamente antes de que el sistema se vuelva inestable."

    a "Voy a recalibrar las neuronas artificiales. Eso debería estabilizar las fluctuaciones, al menos temporalmente."

    dr "De acuerdo, pero hazlo rápido. Cada segundo cuenta. Si el Patriarcado Cyberpunk descubre esta falla, perderemos nuestra ventaja."

    a "Entiendo. Dra. Valentín, ¿realmente cree que podemos derribar el sistema con esta tecnología?"

    dr "No tenemos otra opción, Astrid. Si no lo hacemos nosotros, ¿quién lo hará? Nos vigilan constantemente, pero tenemos una oportunidad única de superarlos."

    a "Voy a transferir los nuevos parámetros al módulo central. Manténgase firme."


    dr "Las lecturas muestran una mejora. Sigue así. Pero no olvides que el menor error podría costarnos caro."

    a "Lo sé, lo sé. Hemos trabajado demasiado duro para fallar ahora."

    show astrid at center with dissolve

    a "Listo. El sistema está estabilizado por ahora. Pero necesitamos encontrar una solución a largo plazo."

    dr "Tienes razón. Esta tecnología es nuestra esperanza, pero debe ser perfecta antes de usarla contra ellos."

    a "Lo lograremos, Dra. Valentín. Juntas, podemos cambiar las cosas."

    dr "Eso espero, Astrid. Por nuestro futuro."

    a "Voy a volver a mis análisis. Todavía hay muchas variables que verificar."

    dr "Y yo me aseguraré de que nuestra cobertura permanezca intacta. Ten cuidado, Astrid."

    a "Usted también, Dra. Valentín."


    # Transition to next scene or end
    scene black with dissolve
    "Unas horas más tarde..."
    return
