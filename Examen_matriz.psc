Algoritmo Examen_matriz
	
	// Definición de variables
	Definir nombreArticulo, matrizFrutas, cantidadFruta, frutaBuscada Como Caracter
	Definir indice Como Entero
	Dimension matrizFrutas[5,2]  // Matriz para almacenar frutas y cantidades
	cantidadFruta = ""
	fruta = ""
	indice = 1
	
	// Mostrar menú inicial
	Escribir "----------------------------------------------"
	Escribir "1.- Para registrar una fruta."
	Escribir "2.- Para buscar una fruta." 
	Escribir "3.- Mostrar las frutas registradas."
	Escribir "4.- Salir del programa."
	Escribir "----------------------------------------------"
	
	Leer opcion
	Mientras opcion <> 4 Hacer
		// Opción 1: Registrar fruta
		Si opcion = 1 Entonces
			Si indice <= 5 Entonces
				Escribir "Ingresa el nombre de la fruta: "
				Leer fruta
				fruta = Minusculas(fruta)
				matrizFrutas[indice,1] = fruta
				Escribir "Ingresa la cantidad: "
				Leer cantidadFruta
				matrizFrutas[indice,2] = cantidadFruta
				indice = indice + 1
			SiNo
				Escribir "No se pueden registrar más frutas."
			FinSi
		FinSi
		
		// Opción 2: Buscar fruta
		Si opcion = 2 Entonces
			Escribir "Ingrese el nombre de la fruta que desea buscar:"
			Leer frutaBuscada
			frutaBuscada = Minusculas(frutaBuscada)
			encontrado = Falso
			Para i Desde 1 Hasta indice - 1 Hacer
				Si matrizFrutas[i,1] = frutaBuscada Entonces
					Escribir "Aquí está la fruta que buscabas:", matrizFrutas[i,1]
					Escribir "Su cantidad es:", matrizFrutas[i,2]
					encontrado = Verdadero
				FinSi
			FinPara
			SI No encontrado Entonces
				Escribir "Fruta no encontrada."
			FinSi
		FinSi
		
		// Opción 3: Mostrar frutas registradas
		Si opcion = 3 Entonces
			Escribir "Frutas registradas:"
			Para i Desde 1 Hasta indice - 1 Hacer
				Escribir "Fruta: ", matrizFrutas[i,1]
				Escribir "Cantidad: ", matrizFrutas[i,2]
			FinPara
		FinSi
		
		// Opción no válida
		SI No (opcion = 1 O opcion = 2 O opcion = 3) Entonces
			Escribir "Opción incorrecta. Por favor, ingrese una opción válida."
		FinSi
		
		// Mostrar menú nuevamente
		Escribir "----------------------------------------------"
		Escribir "1.- Para registrar una fruta."
		Escribir "2.- Para buscar una fruta." 
		Escribir "3.- Mostrar las frutas registradas."
		Escribir "4.- Salir del programa."
		Escribir "----------------------------------------------"
		Leer opcion
	FinMientras
	
FinAlgoritmo