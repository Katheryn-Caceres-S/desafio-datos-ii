# sistema de notas
# 1 ingresar notas
# calcualr estadirsta de las notas
# notas mas bajos
# cantidad de aprobados
# menu


"""definir el menu"""
def menu():
    print("""
Menu de opciones
1. Ingresar Nota
2. Calcular estadisticas
3. Resultados
4. Salir          
""")

"""la buena practica dice que debe tener el mismo nombre del archivo"""
def main():
    """variable vacia del tipo lista"""
    notas = []  

    while True:
        menu()
        opcion = input("ingrese una opcion ")

        if opcion == "1":
            n = input("ingresa las notas (el formato debe ser ingresado con espacios 7.0 3.5 6.7)")
            """para ingresar varias"""
            n = n.split(" ")
            print("1")
            break
        elif opcion == "2":
            print ("2")
            break
        elif opcion == "3":
            print ("3")
        else:
            print("terminado")
            break

"""con esto se llama a la funcion, para que corra"""
""" el if dicce que solo corre si el archivo se llama main, es para que solo corra en este archivo"""
if __name__ == "__main__":
    main ()