from random import randint

print("-----------------------------------------------------------------------------")
print("¡Hola, Bienvenido al juego, intenta adivinar el número que he pesando!")
print("-----------------------------------------------------------------------------")
nombre=input("¿Cómo te llamas?: ")

aleatorio = randint(1,100)
intentos_realizados= 0
intentos_max = 8

print("---------------------------------------------------------------------------------------------------------------------------")
print(f"Bueno,{nombre}, he pensado un número entre 1 y 100, y tenés solo ocho intentos para adivinar cuál crees que es el número")

while intentos_realizados < intentos_max:
        numero = input("Elige un número: ")
        numero = int(numero)
        intentos_realizados += 1

        if numero == aleatorio:
            print(F"Has adivinado el número, eres un genio {nombre}! lo lograste en {intentos_realizados} intentos.")
            break
        if numero > 100 and numero < 1:
            print("un número que no elegiste no está permitido")
        elif numero > aleatorio:
            print("Te pasaste, el número que elegiste es más grande que el número secreto!")
        elif numero < aleatorio:
            print("fallaste!, el número que elegiste es menor que el número secreto!")
        else:
            print(f"Lo siento, {nombre}. No has adivinado el número secreto {aleatorio}. ¡Mejor suerte la próxima vez!")
