import random


def obtener_palabra_secreta() -> str:
    palabras = ["python", "javascript", "django", "java", "react", "git", "typescript"]
    return random.choice(palabras)


def mostrar_avance(palabra_secreta, letras_adivinadas):
    adivinado = ""

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"

    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("Bienvenido al juego de ahorcado")
    print(f"Tenés {intentos} intentos para adivinar la palabra secreta")
    print(
        mostrar_avance(palabra_secreta, letras_adivinadas),
        "la cantidad de letras de la palabra es:",
        len(palabra_secreta),
    )

    while not juego_terminado and intentos > 0:
        adivinanza = input("introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra válida")
        elif adivinanza in letras_adivinadas:
            print("ya has utilizado esa letra prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(
                    f"Has acertado! la letra '{adivinanza}' está presente en la palabra"
                )
            else:
                intentos -= 1
                print(
                    f"lo siento mucho la letra '{adivinanza}' no está presente en la palabra secreta"
                )
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostrar_avance(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(
                f"Felicitaciones has ganado! la palabra completa es: '{palabra_secreta}'"
            )

    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(
            f"Lo sentimos mucho se te han acabado los intentos, la palabra secreta era '{palabra_secreta}'"
        )


juego_ahorcado()
