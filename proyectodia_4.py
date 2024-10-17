from random import randint

print("-----------------------------------------------------------------------------")
print("¡Hola, Bienvenido al juego, intenta adivinar el número que he pensado!")
print("-----------------------------------------------------------------------------")

while True:
    nombre = input("¿Cómo te llamas?: ")
    aleatorio = randint(1, 100)
    intentos_realizados = 0
    intentos_max = 8

    print("---------------------------------------------------------------------------------------------------------------------------")
    print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tenés solo ocho intentos para adivinar cuál crees que es el número.")

    while intentos_realizados < intentos_max:
        numero = input("Elige un número: ")
        numero = int(numero)

        if numero < 1 or numero > 100:
            print("El número que elegiste no está permitido.")
        elif numero == aleatorio:
            print(f"¡Has adivinado el número, eres un genio {nombre}! Lo lograste en {intentos_realizados} intentos.")
            break
        elif numero > aleatorio:
            print("Te pasaste, el número que elegiste es más grande que el número secreto!")
        elif numero < aleatorio:
            print("¡Fallaste! El número que elegiste es menor que el número secreto!")
        intentos_realizados += 1
    else:
        print(f"Lo siento, {nombre}. No has adivinado el número secreto {aleatorio}. ¡Mejor suerte la próxima vez!")

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ")
    if jugar_de_nuevo != 'sí':
        print("¡Gracias por jugar! Hasta la próxima.")
        break