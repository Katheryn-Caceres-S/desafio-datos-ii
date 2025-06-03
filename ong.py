

#Crear un script llamado ong.py que contenga las siguientes funciones:
# Una función que calcule el factorial.
# Una función que calcule la productoria.
# Una función que permita controlar los cálculos. Esta función se debe invocar de la siguiente manera:
#calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

""" Calcula el factorial de un número"""
def factorial(n: int) -> int:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

"""Calcula la productoria de una lista de enteros"""
def productoria(lista: list[int]) -> int:
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

"""Recibe múltiples argumentos nombrados y calcula factorial o productoria"""
def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if "fact" in clave:
            resultado = factorial(valor)
            print(f"El factorial de {valor} es {resultado}")
        elif "prod" in clave:
            resultado = productoria(valor)
            print(f"La productoria de {valor} es {resultado}")
        else:
            print(f"Parametro desconocido: {clave}")

if __name__ == "__main__":
    #Prueba 1
    print("Prueba 1")
    calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)

    #Prueba 2
    print("Prueba 2")
    calcular(fact_1=1, prod_1=[1, 2, 3, 4, 5], fact_2=2)

    #Prueba 3
    print("Prueba 3")
    calcular(fact_1=8, prod_1=[10, 100, 20, 300, 800], fact_2=12)

# estoy con la duda de como ingresar los valores fuera, es decir desde la terminal.
#   