Algoritmo Examen_vectores
	definir n Como Entero
	
	contadorm5 = 0
	suma = 0
	
	Escribir "Ingresa la cantidad de números a evaluar: "
	leer n
	
	Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Ingrese el número ", i, ":"
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
            contadorm5 = contadorm5 + 1 // números  mayores que 5.
        FinSi
		
        suma = suma + num // suma de todos los números.

		
	FinPara
	Escribir "El número mayor es: ", mayor
	Escribir "El número menor es: ", menor
	Escribir "La cantidad de números mayores que 5 es: ", contadorm5
	Escribir "La suma de todos los números es: ", suma
FinAlgoritmo
