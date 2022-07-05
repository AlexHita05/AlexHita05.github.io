# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Desconocido")

image Desconocido = "Desconocido.png"

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene afueras with fade:


    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.


    show Desconocido at right:
        zoom 0.6

    # Presenta las líneas del diálogo.

    "He vuelto a hacerlo, se que no debo pero, he regresado."

    "Aquí estoy de nuevo, otra madrugada más en la puerta, como si fuera un asaltante en mi propia casa."

menu:
    "Atravesar puerta":
        jump scene2

    "Marcharse, de nuevo":
        return


label scene2:

    scene door open with fade:
        zoom 0.51

    "Atravieso la puerta, pese al cargo de conciencia, no debo, lo hago igual."

label sceneblack:

    scene pasillo with fade:
        zoom 1.1

menu:
    "Entrar al salón":
        jump scenesalon

    "Entrar a la cocina":
        jump scenecocina


label scenesalon:

    scene baile 2 with fade:
        zoom 0.5


    "Intacto en el recuerdo, permanente en el tiempo."

    "Encima de la televisión, una fotografía apoyada."

    "Bailábamos, tu reías, las gaviotas celos chirriaban."

    "¿Quién podría habernos separado, siendo tan inmortales?"

menu:
    "Ir a la puerta del dormitorio":
        jump scene3

    "Ir a la cocina":
        jump scenecocina

label scenecocina:

    scene cocina with fade:
        zoom 0.7

    "Media tarrina de helado de vainilla,"

    "eso es lo que ahora cenas."

    "Ni siquiera lo has regresado al congelador."

    "¿Es la desgana tu nueva inquilina?"

    "Espero que al menos eches de menos mi cuscús al limón."


menu:
    "Ir a la puerta del dormitorio":
        jump scene3

    "Entrar al salón":
        jump scenesalon





label scene3:

    scene puerta dormitorio with fade:
        zoom 0.45

    "Me paro enfrente de la puerta de nuestro dormitorio, su dormitorio."

    "No debo hacerlo, lo hago igual."

    "Siempre me topo con el mismo miedo,"

    "a verla con otro hombre ocupando mi espacio, mi lugar,"

    "mi colchón, su corazón, su placer, sus pensamientos."

    "No puedo evitar ser egoísta, y estúpido, un estúpido egoísta,"

    "qué más da, no tengo derecho."

menu:
    "Entrar al dormitorio":
        jump scene4

    "Marcharse, de nuevo":
        return

label scene4:

    scene ella 2 with fade:
        zoom 0.75


    "Respiro aliviado."

    "Ahí está, durmiendo abrazada a la almohada,"

    "el rostro tenuemente iluminado por la poca luz que la luna de agosto arroja por la ventana."

    "abierta de par en par, persiana inexistente."

    "Siempre fue una discusión recurrente,"

    "yo tan opaco y ella tan fúlgida."

    "Al final solo ha quedado luz."

menu:
    "Acercarse":
        jump scene5

    "Me marcho, de nuevo":
        return

label scene5:

    scene ella with fade:


    "Me acerco, la observo."
    "Su saliva en la almohada, en mi boca una sonrisa."
    "Quiero tocarte, pero no puedo."
    "Quiero besarte, pero no puedo."
    "Suspiro."
    "La nostalgia se convertiría en lágrima, pero llorar no puedo."
    "Te echo de menos, eso sí que puedo."

menu:
    "Observar escritorio":
        jump sceneescritorio

    "Observar mesita de noche":
        jump scenemesita

    "Observar cajas apiladas":
        jump scenecajas


    "Marcharse, de nuevo":
        return

label sceneescritorio:

    scene escritorio with fade:
        zoom 0.8

    "La mesa ya no está repleta de periódicos, de mis redacciones y artículos."

    "Hace tanto que no escribo, que no esbozo mi amor por el periodismo."

    "También lo echo de menos, aunque quizás le dediqué demasiado tiempo,"

    "tiempo que no invertí en ella, en grandes proyectos de futuro que jamás se cumplirán."

    "Aunque siendo egoísta, no me arrepiento, pues mis escrituras son las que me mantienen vivo."

menu:

    "Observar pantalla del ordenador":
        jump sceneordenador

    "Observar mesita de noche":
        jump scenemesita

    "Observar cajas apiladas":
        jump scenecajas

    "Rehusar marcharse":
        jump scenerehusar

    "Marcharse, de nuevo":
        return

label scenemesita:

    scene cenicero with fade:
        zoom 0.8

    "En la mesita, como se ha hecho costumbre desde que me fui, el cenicero lleno de colillas."

    "Extraño fumarme un cigarrillo,"

    "me encantaba esa banal pero agradable sensación de dejar escapar el humo entre mis labios."

    "El morbo de apuñalarme con cada calada."

    "Al final, no es ella tan diferente de la nicotina."

    "No es la vida tan diferente de un cigarro."

menu:
    "Observar escritorio":
        jump sceneescritorio

    "Observar cajas apiladas":
        jump scenecajas

    "Rehusar marcharse":
        jump scenerehusar

    "Marcharse, de nuevo":
        return


label scenecajas:

    scene cajas with fade:

    "Que extraño me resulta ver nuestra habitación, su habitación, sin mis cosas."

    "A un lado de la mesa cuatro cajas obstaculizan la apertura del armario."

    "En ellas está mi nombre escrito. Supongo que empaquetar y deshacer es parte del olvido."

    "No la culpo, yo habría hecho lo mismo."


menu:
    "Observar escritorio":
        jump sceneescritorio

    "Observar mesita de noche":
        jump scenemesita

    "Rehusar marcharse":
        jump scenerehusar

    "Marcharse, de nuevo":
        return


label sceneordenador:

    scene accidente with fade:
        zoom 1.2

    "El Nocturno: 21 de julio de 2020"

    "FALLECE UN CONDUCTOR TRAS CHOCAR FRONTALMENTE CONTRA UN CAMIÓN"

    "Un conductor ha fallecido esta madrugada tras chocar frontalmente contra un camión."

    "Al parecer, el conductor fallecido ha invadido el carril contrario provocando el trágico desenlace."

    "El conductor del camión está ingresado con diversas heridas con pronóstico grave."

    "Las primeras hipótesis barajan que la ingesta de alcohol por parte del piloto fallecido

    podría haber sido una de las consecuencias del trágico accidente."




menu:

    "Observar cajas apiladas":
        jump scenecajas

    "Observar mesita de noche":
        jump scenemesita

    "Rehusar marcharse":
        jump scenerehusar

    "Marcharse, de nuevo":
        return


label scenerehusar:

    scene rehusar with fade:



    "¿Y si me quedo para siempre?,"

    "¿y si me niego a irme?"

    "Siempre fui en contra de lo establecido,"

    "¿por qué no debería pues hacerlo ahora?"

    "Siempre fui caprichoso,"

    "siempre antepuse mi propio beneficio al de los demás,"

    "siempre pensé tan solo en mí."

    "Hasta ahora."

    "He de irme, no debo quedarme, no puedo quedarme."

    "Me juro que esta madrugada habrá sido la última vez, no volveré."

    "Tengo que dar el paso, he de olvidar, dejar estar, dejar en paz."

    "Quizá dentro de un tiempo nos podamos reencontrar, pero no por ahora,"

    "al menos eso espero."

menu:

    "Marcharse, de nuevo":
        jump scenemarcharse

    "Marcharse, de nuevo":
        jump scenemarcharse


label scenemarcharse:

    scene accidente 2 with fade:
        zoom 1.1



    "Maldigo aquella fatídica noche en la que me separé de ella."

    "Verla llorando rompió lo que ya estaba roto."

    "Aún me siento absurdo."

    "No entiendo cómo, si ya sabía las consecuencias, si ya había escrito sobre ello."

    "Cada semana llegaban a la redacción casos sobre nuevos accidentes en los que el homicida había sido el alcohol, o la irresponsabilidad, o los dos."

    "Ya sabía qué podía pasar."

    "Ver mi rostro estampado en el volante."

    "Las sirenas, los walkie-talkies."

    "No quedaba más que vislumbrar aquella macabra obra escénica, asumiendo que no había retorno."

    "De este fallo no se aprende, no tuve oportunidad para ello."

jump scenesola


label scenesola:

    scene sola with fade:
        zoom 0.4


    "A ella la abandoné, la dejé desconsolada, marchita, mustia."

    "Observarla en mi funeral tan solo cercioró mi más incesante temor,"

    "esa noche no solo había muerto yo."

    "Espero que pueda perdonarme algún día."

    return
