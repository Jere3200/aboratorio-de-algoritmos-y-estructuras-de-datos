print("--------------------------------------------------------------------")
print("Ingresando al sistema cálculador de comisiones de Westfast SA. ")
print("--------------------------------------------------------------------")


print("Has ingresado con éxito")

nombre=input("Ingresa tu nombre, por favor: ")
print(f"Hola {nombre}, gracias por ingresar en el sistema, cuentame cuanto has vendido este mes en valor númerico. ")

vendido=input("Ingresa el valor vendido, por favor: $")

vendido=float(vendido)

totalcomision=(vendido*0.13)

print(F"Wow! {nombre}, vendiste ${vendido}, de la cual lograste una excelente comisión del 13%, que como resultado fue ${totalcomision}")
print("Sigue así, felicitaciones!")

