import random

palabras=["universidad","estadio","pelota","computadora"] # lista de palabras para el juego.

def elegir_palabra(): #función para elegir una palabra al azar.
    return random.choice(palabras)

def pedir_letra(): # función para solicitar ingresar una letra, se verifica que sea válida y la pasamos a minúsculas.
    while True:
        letra = input("Elige una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Por favor, ingresa una sola letra válida.")

def mostrar_progreso(palabra, letras_adivinadas): # función para mostrar el progreso y letras adivinadas.
    progreso = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    print("Progreso:", progreso)


def juguemos():#función para empezar el juego

    palabra_secreta = elegir_palabra()
    letras_adivinadas = set() # eliminamos los duplicados.
    vidas = 6

    def saludar():# función para saludar al jugador.

        print("Gracias por jugar, saludos Jeremías.")
        print(
            '\n░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░'
            '\n░░░░░░░░░░░█░░█░░░░░░░░░░░░░'
            '\n░░░░░░░░░░░█░░█░░░░░░░░░░░░░'
            '\n░░░░░░░░░░█░░░█░░░░░░░░░░░░░'
            '\n░░░░░░░░░█░░░░█░░░░░░░░░░░░░'
            '\n██████▄▄█░░░░░██████▄░░░░░░░'
            '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
            '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
            '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
            '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
            '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
            '\n▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░'
            '\n█████▀░░░░▀▀████████░░░░░░░░'
            '\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        )

    print("---------------------------------------------------------------------------------------")
    print("¡Bienvenido al Ahorcado!")
    print(f"Tienes '6' vidas en  total. Adivina la palabra sin perder todas tus vidas! ")
    print("Muchas suerte!")
    print("---------------------------------------------------------------------------------------")
    while vidas > 0: # comienzo ciclo de juego.
        mostrar_progreso(palabra_secreta, letras_adivinadas)

        letra = pedir_letra()

        if letra in letras_adivinadas: #corroboramos que no ingrese la misma letra.
            print("Ya has adivinado esa letra. Prueba con otra mejor.")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra_secreta: # acierto de la letra ingresada en la palabra al azar.
            print(f"Acertaste! La letra '{letra}' está en la palabra.")
        else:
            vidas -= 1
            print("Letra incorrecta. Te quedan", vidas, "vidas.") # fallo de la letra ingresada en la palabra al azar.

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("¡Felicidades! Has adivinado la palabra que era:", palabra_secreta) #adivino la palabra.
            saludar()
            break
    else:
        print("Has perdido, más suerte la próxima. La palabra era:", palabra_secreta) # el usuario perdió.
        saludar()


# Iniciar el juego
juguemos()