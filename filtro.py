# esto es una lista
# agregar el sysarg

import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

"""" Crear la funcion"""
# (despues de los dos puntos, le decimos que es diccionario del tipo str y int)
#( modo va a ser siempre MAYOR a menos que se entregue otro)

def filtro(precios:dict[str,int], umbral:int, modo:str= "mayor"):
    if modo == "mayor":
        mayores = []
        """"para cada llave, valor en los items de precios"""
        for k,v in precios.items():
            """"si el valor es mayor al umbral, se imprime...append funciona para lista y no diccionarios {}"""
            if v > umbral:
                mayores.append(k)

        print("Los productos mayores al umbral son:" , mayores)

    #filtro menores
    elif modo == "menores":
        menores = []
        """"para cada llave, valor en los items de precios"""
        for k,v in precios.items():
            """"si el valor es menor al umbral, se imprime...append funciona para lista y no diccionarios {}"""
            if v < umbral:
                menores.append(k)
        print("Los productos menores al umbral son: ", menores)

    else:
        print("lo sentimos, esto no es valido")

    return

def main():
    if len(sys.argv) < 2:
        print("python filtro.py 'umbral'")
        sys.exit(1)
    try:
        umbral = int(sys.argv[1])
    except ValueError:
        print("El umbral debe ser un número entero.")
        sys.exit(1)

    modo = sys.argv[2] if len(sys.argv) > 2 else "mayor"

    filtro(precios, umbral, modo)

if __name__ == "__main__":
    main()