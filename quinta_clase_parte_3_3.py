def cero_dos_veces(*args):
    for i in range(len(args)-1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
        return False

numeros = input("Ingresa los números que desees separados por comas: ")
numeros_lista= [int(num) for num in numeros.split(",")]

resultado = cero_dos_veces(*numeros_lista)
print(resultado)

