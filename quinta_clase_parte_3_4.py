def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def contar_primos(num):
    cantidad_primos = 0

    for i in range(num + 1):
        if es_primo(i):
            print(i)
            cantidad_primos += 1

    return cantidad_primos

numero_usuario = int(input("Ingresa un número: "))


resultado = contar_primos(numero_usuario)
print(f"\nCantidad de números primos encontrados: {resultado}")