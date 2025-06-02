# sistema de notas
# 1 ingresar notas
# calcualr estadirsta de las notas
# notas mas bajos
# cantidad de aprobados
# menu


from notas.menu import menu
from notas.ingresar_notas import ingresar_notas

"""la buena practica dice que debe tener el mismo nombre del archivo"""
def main():
    """variable vacia del tipo lista"""
    notas = []  

    while True:
        menu()
        opcion = input("ingrese una opcion ")

        if opcion == "1":
            ingresar_notas()
            print(f"notas ingresadas son {notas: }")


        elif opcion == "2":


        elif opcion == "3":
            """esto para mostrar resultados en pantalla"""
            print (f"""
promedio : {promedio}
minimo   : {menor}
mayo     : {mayor}
aprobado : {aprobado}
""")
        else:
            print("terminado")
            break

"""con esto se llama a la funcion, para que corra"""
""" el if dicce que solo corre si el archivo se llama main, es para que solo corra en este archivo"""
if __name__ == "__main__":
    main ()