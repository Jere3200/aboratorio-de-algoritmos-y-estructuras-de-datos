Algoritmo Examen_vectores
	definir n Como Entero
	
	contadorm5 = 0
	suma = 0
	
	Escribir "Ingresa la cantidad de n�meros a evaluar: "
	leer n
	
	Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Ingrese el n�mero ", i, ":"
        Leer num
		
		
        Si i = 1 Entonces
            mayor = num
            menor = num
        SiNo
            Si num > mayor Entonces // numero mayor.
                mayor = num
            FinSi
            Si num < menor Entonces // numero menor.
                menor = num
            FinSi
        FinSi
		
        Si num > 5 Entonces
            contadorm5 = contadorm5 + 1 // n�meros  mayores que 5.
        FinSi
		
        suma = suma + num // suma de todos los n�meros.

		
	FinPara
	Escribir "El n�mero mayor es: ", mayor
	Escribir "El n�mero menor es: ", menor
	Escribir "La cantidad de n�meros mayores que 5 es: ", contadorm5
	Escribir "La suma de todos los n�meros es: ", suma
FinAlgoritmo
