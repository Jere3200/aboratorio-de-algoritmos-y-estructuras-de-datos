# Bienvenida al usuario.
print("----------------------------------------------------------------------------------------------------")
print("Hola, ¿Cómo estás? Un gusto saludarte, usuario. ¡Bienvenido al mejor sistema de análisis de nombres!")
print("----------------------------------------------------------------------------------------------------")
print("--------------------------------------- ¡COMENZEMOS! -----------------------------------------------")

# Declaración de variables.
nombres = []

# Comienzo del ciclo para carga de nombres.
while True:
    nombre = input("Ingresa los nombres de los estudiantes que desees.\n"
                   "----------------------------------------------------------------------------------------------------\n"
                   "Utiliza 'FIN' para terminar la carga, y 'REPETIR' para ver los ya ingresados.\n"
                   "Ingresa el nombre aquí: ").strip()

    # Convertimos a minúsculas para la comparación.
    nombre_lower = nombre.lower()

    # 1. Ingreso de nombres con la opción de detener con "FIN".
    if nombre_lower == "fin":
        break

    # 2. Opción "REPETIR" para mostrar los nombres ingresados. / Convertimos a minúsculas para la comparación.
    elif nombre_lower == "repetir":
        print("----------------------------------------------------------------------------------------------------")
        if nombres:
            print(f"Los nombres cargados son: {nombres}")
        else:
            print("No se han ingresado nombres aún.")
        print("----------------------------------------------------------------------------------------------------")

    # 3. Validación de nombres.
    elif nombre.isdigit():
        print("El nombre no puede ser un número.")
    # permite la carga de nombres compuesto, elimina los espacios y verifica que los caracteres sean alfabeticos.
    elif nombre.replace(" ", "").isalpha() and nombre.strip():
        nombres.append(nombre)
        print(f"Nombre '{nombre}' agregado correctamente, muy bien! .")
    else:
        print("El nombre es inválido. Por favor, prueba cargando un nombre válido.")

print("----------------------------------------------------------------------------------------------------------------")
print("Excelente, ahora pasemos a mi menú interactivo, te mostraré lo que podemos hacer con los nombres que cargaste!")

# Menú de opciones interactivo.
while True:
    print("----------------------------------------------------------------------------------------------------------------")
    print("Menú de Opciones.")
    print("----------------------------------------------------------------------------------------------------------------")
    print("1.- Mostrar nombres ingresados.")
    print("2.- Ordenar los nombres alfabéticamente.")
    print("3.- Análisis de longitud: mostrar el nombre más largo y el más corto.")
    print("4.- Contar vocales y consonantes en los nombres combinados.")
    print("5.- Contar palabras en cada nombre.")
    print("6.- Inversión de los nombres.")
    print("7.- Mostrar nombres que empiezan con una letra específica.")
    print("8.- Buscar si un nombre está en la lista.")
    print("9.- Contar cuántos nombres tienen más de 5 caracteres.")
    print("10.- Convertir todos los nombres a mayúsculas o minúsculas.")
    print("11.- Salir del programa.")
    print("----------------------------------------------------------------------------------------------------------------")
    print("FUNCIONES ADICIONALES AGREGADAS.")
    print("----------------------------------------------------------------------------------------------------------------")
    print("12.- Eliminar un nombre de la lista.")
    print("----------------------------------------------------------------------------------------------------------------")
    seleccion = input("Ingresa la opción que desees: ")

    # 4. Mostrar nombres ingresados.
    if seleccion == "1":
        print(f"Los nombres ingresados fueron: {nombres}.")

    # 5. Ordenar los nombres alfabéticamente.
    elif seleccion == "2":
        nombres_minusculas = [nombre.lower() for nombre in nombres]
        nombres_ordenados = sorted(nombres_minusculas)
        print("Nombres ordenados alfabéticamente:", nombres_ordenados)

    # 6. Análisis de longitud: mostrar el nombre más largo y el más corto.
    elif seleccion == "3":
        if nombres:  # Verifica que la lista no esté vacía
            nombre_mas_largo = max(nombres, key=len)
            nombre_mas_corto = min(nombres, key=len)
            print(f"El nombre más largo es: {nombre_mas_largo}")
            print(f"El nombre más corto es: {nombre_mas_corto}")
        else:
            print("No hay nombres para analizar.")

    # 7. Contar vocales y consonantes en los nombres combinados.
    elif seleccion == "4":
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

        total_vocales = total_consonantes = 0

        for nombre in nombres:
            for letra in nombre:
                if letra in vocales:
                    total_vocales += 1
                elif letra in consonantes:
                    total_consonantes += 1
        print(f"La cantidad de vocales es: {total_vocales}")
        print(f"La cantidad de consonantes es: {total_consonantes}")

    # 8. Contar palabras en cada nombre.
    elif seleccion == "5":
        for nombre in nombres:
            cantidad_palabras=len(nombre.split())
            print(nombre,"tiene",cantidad_palabras,"palabras. ")
        contar_palabras = sum(len(nombre.split()) for nombre in nombres)
        print(f"El total de palabras es: {contar_palabras}")


    # 9. Inversión de los nombres.
    elif seleccion == "6":
        invertir_nombres = nombres[::-1]
        nombres_invertidos = [nombre[::-1] for nombre in nombres]
        print(f"Los nombres invertidos se ven así: {invertir_nombres}.")
        print(f"Los nombres con los caracteres invertidos son:{nombres_invertidos}")
        print("Se ve gracioso, ¿No?, jajaja.")

    # 10. Mostrar nombres que empiezan con una letra específica.
    elif seleccion == "7":
        letra_buscar = input("Ingresa la letra que quieras averiguar: ").upper()
        nombres_letra = [nombre for nombre in nombres if nombre.upper().startswith(letra_buscar)]

        if nombres_letra:
            print(f"Los nombres que empiezan con '{letra_buscar}' son:", nombres_letra)
        else:
            print(f"No hay nombres que empiecen con '{letra_buscar}'.")

    # 11. Buscar si un nombre está en la lista.
    elif seleccion == "8":
        nombre_busqueda = input("Ingresa el nombre que quieras buscar: ").upper()
        nombres_upper = [nombre.upper() for nombre in nombres]

        if nombre_busqueda in nombres_upper:
            print(f"El nombre '{nombre_busqueda}' está en la lista.")
        else:
            print(f"El nombre '{nombre_busqueda}' no está en la lista.")

    # 12. Contar cuántos nombres tienen más de 5 caracteres.
    elif seleccion == "9":
        nombres_largos = [nombre for nombre in nombres if len(nombre) > 5]
        contador_nombres_largos = len(nombres_largos)
        print(f"Cantidad de nombres con más de 5 caracteres son: {contador_nombres_largos}")
        if contador_nombres_largos > 0:
            print("Nombres:", nombres_largos)

    # 13. Convertir todos los nombres a mayúsculas o minúsculas.
    elif seleccion == "10":
        nombres_mayusculas = [nombre.upper() for nombre in nombres]
        nombres_minusculas = [nombre.lower() for nombre in nombres]

        print("Nombres en mayúsculas:", nombres_mayusculas)
        print("Nombres en minúsculas:", nombres_minusculas)

    elif seleccion == "12":
        print(f"Los nombres cargados son {nombres}.")
        eliminar_nombre = input("¿Qué nombre querés deseas eliminar?: ").upper()
        nombres = [nombre.upper() for nombre in nombres]
        if eliminar_nombre in nombres:
            nombres.remove(eliminar_nombre)
            print(f"{eliminar_nombre} ha sido borrado.")
            print(f" La lista actualizada es: {nombres}")
        else:
            print(f"{eliminar_nombre} no está en la lista.")

    # Salir del programa.
    elif seleccion == "11":
        print("----------------------------------------------------------------------------------------------------------------")
        print("Ha sido un gusto que utilizarás mi programa, ¡espero verte pronto!")
        print("Saludos, Jeremias!")
        print(""
              '\n░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░'
              '\n░░░░░░░░░░░█░░█░░░░░░░░░░░░░'
              '\n░░░░░░░░░░░█░░█░░░░░░░░░░░░░'
              '\n░░░░░░░░░░█░░░█░░░░░░░░░░░░░'
              '\n░░░░░░░░░█░░░░█░░░░░░░░░░░░░'
              '\n██████▄▄█░░░░░██████▄░░░░░░░'
              '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
              '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
              '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
              '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
              '\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░'
              '\n▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░'
              '\n█████▀░░░░▀▀████████░░░░░░░░'
              '\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
              '\n╔════╗░░╔════╗╔═══╗░░░░░░░░░'
              '\n║████║░░║████║║███╠═══╦═════╗'
              '\n╚╗██╔╝░░╚╗██╔╩╣██╠╝███║█████║'
              '\n░║██║░░░░║██║╔╝██║███╔╣██══╦╝'
              '\n░║██║╔══╗║██║║██████═╣║████║'
              '\n╔╝██╚╝██╠╝██╚╬═██║███╚╣██══╩╗')
        break

    else:
        print("Opción inválida. Por favor, elige una opción válida.")