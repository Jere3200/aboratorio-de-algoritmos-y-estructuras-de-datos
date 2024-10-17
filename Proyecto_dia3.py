texto=input("Hola Usuario, bienvenido. Ingresar un texto de tu preferencia: ")
print("Excelente, ahora ingresa 3 letras diferentes para mostrarte que puedo hacer con ello. ")

letra1=input("Ingresa la primera letra: ")
letra2=input("Ingresa la segunda letra: ")
letra3=input("Ingresa la tercer letra: ")

#1¿cuántas veces aparece cada una de las letras que eligió?
contador1=texto.count(letra1)
contador2=texto.count(letra2)
contador3=texto.count(letra3)

#2¿cuántas palabras hay a lo largo de todo el texto?
palabrastexto=texto.split()
resultado_palabras=len(palabrastexto)

#3¿cuál es la primera letra del texto y cuál es la última?
inicio=texto[0]
fin=texto[-1]
#4mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
invetir=texto[::-1]

#5decir si la palabra “Python” se encuentra dentro del texto.


print("Acá tienes el resultado del análisis en tu texto:")
print("-----------------------------------------------------------------")
print(f"la letra {letra1} aparece {contador1} veces en el texto.")
print(f"la letra {letra2} aparece {contador2} veces en el texto.")
print(f"la letra {letra3} aparece {contador3} veces en el texto.")
print("-----------------------------------------------------------------")
print(f"El texto tiene {resultado_palabras} palabras")
print("-----------------------------------------------------------------")
print(f"La primera letra de tu texto es: {inicio}")
print(f"La última letra de tu texto es: {fin}")
print("-----------------------------------------------------------------")
print(f"Tu texto invertido se ve así: {invetir}")
print("-----------------------------------------------------------------")
if "Python" in texto:
    print("La palabra Python se encuentra en el texto. ")
else:
    print("La palabra Python no se encuentra en el texto. ")