def letras_organizadas(palabras):
    letras=set(palabras)

    letras_ordenadas=sorted(letras)
    return letras_ordenadas

palabra=input("Ingresa una palabra: ").upper()

resultado=letras_organizadas(palabra)
print(resultado)


