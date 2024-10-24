def devolver_distintos(a, b, c):
    suma = a + b + c

    if (a >= b and a <= c) or (a <= b and a >= c):
        intermedio = a
    elif (b >= a and b <= c) or (b <= a and b >= c):
        intermedio = b
    else:
        intermedio = c

    mayor = max(a, b, c)
    menor = min(a, b, c)

    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else:
        return intermedio

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

resultado = devolver_distintos(num1, num2, num3)
print(f"El resultado es: {resultado}")