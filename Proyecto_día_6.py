import os
from pathlib import Path


# Definición de funciones para el uso correcto del programa.

def limpiar_pantalla():  # Función limpiar pantalla.
    os.system('cls' if os.name == 'nt' else 'clear')


def contar_recetas():  # Función contar cantidad de recetas totales en la carpeta madre de las recetas.
    total = 0
    for categoria in Path("Recetas").iterdir():
        if categoria.is_dir():
            total += len(list(categoria.glob("*.txt")))
    return total


def mostrar_menu():  # Función menú de opciones.
    print("---------------------------------------------------")
    print("Bienvenido al administrador de recetas!")
    print("Ruta de acceso:", Path("Recetas"))
    print("Total de recetas:", contar_recetas())
    print("Por favor, elige una opción:")
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir")
    print("---------------------------------------------------")

def leer_receta(): # función leer receta.
    categoria = elegir_categoria()
    receta = elegir_receta(categoria)
    with open(categoria / receta, 'r') as file:
        print(file.read())


def crear_receta(): # función crear la receta.
    categoria = elegir_categoria()
    nombre = input("Ingrese el nombre de la receta: ")
    contenido = input("Ingrese el contenido de la receta: ")
    receta_path = categoria / f"{nombre}.txt"
    with open(receta_path, 'w') as file:
        file.write(contenido)


def crear_categoria(): # función crear categoría.
    nombre = input("Ingrese el nombre de la nueva categoría: ")
    categoria_path = Path("Recetas") / nombre
    categoria_path.mkdir(exist_ok=True)


def eliminar_receta(): # función eliminar receta.
    categoria = elegir_categoria()
    receta = elegir_receta(categoria)
    (categoria / receta).unlink()
    print("Receta eliminada.")


def eliminar_categoria(): # función eliminar categoría.
    categorias = [d for d in Path("Recetas").iterdir() if d.is_dir()]
    print("Categorías: ", [categoria.name for categoria in categorias])
    nombre = input("Ingrese el nombre de la categoría a eliminar: ")
    categoria_path = Path("Recetas") / nombre
    for receta in categoria_path.glob("*.txt"):
        receta.unlink()
    categoria_path.rmdir()
    print("Categoría eliminada.")


def elegir_categoria(): #  función elegir categoría.
    categorias = [d for d in Path("Recetas").iterdir() if d.is_dir()]
    print("Categorías: ", [categoria.name for categoria in categorias])
    nombre_categoria = input("Elija una categoría: ")
    return Path("Recetas") / nombre_categoria


def elegir_receta(categoria): # función elegir receta.
    recetas = list(categoria.glob("*.txt"))
    print("Recetas: ", [receta.name for receta in recetas])
    nombre_receta = input("Elija una receta: ") + ".txt"
    return nombre_receta


def main():
    while True: # comienzo del ciclo.
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Ingresa tu opción: ")

        # Preguntar si el usuario realmente quiere continuar con la opción seleccionada.
        print("----------------------------------------------------------------------------")
        confirmar = input("¿Estás seguro de que desea continuar con esta opción? (si/no): ")
        print("----------------------------------------------------------------------------")
        if confirmar.lower() != 'si':
            continue  # Si no está seguro, regresa al menú

        if opcion == '1':  # Leer receta.
            leer_receta()
        elif opcion == '2':  # Crear receta.
            crear_receta()
        elif opcion == '3':  # Crear categoría
            crear_categoria()
        elif opcion == '4':  # Eliminar receta.
            eliminar_receta()
        elif opcion == '5':  # Eliminar categoría.
            eliminar_categoria()
        elif opcion == '6':  # Salir.
            print("----------------------------------------------------------------------------")
            print("Saliendo del programa.")
            print("Gracias por jugar, saludos Jeremías.")
            print(
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
            )
            break
        else:
            print("----------------------------------------------------------------------------")
            print("Opción no válida.")
            print("----------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------")
        input("Presiona una tecla para acceder al menú nuevamente: ")
        print("----------------------------------------------------------------------------")


# Llamada a la función main, fuera de su definición.
if __name__ == "__main__":
    main()
