

def ingresar_notas() -> list[float]:
    """ 
    solicita al usuario ingresar notas separadas por espacio
    Se separan y se transforman en una lista de flotantes
    """

    n = input("ingresa las notas (el formato debe ser ingresado con espacios 7.0 3.5 6.7)")
    """para ingresar varias notas"""
    n = n.split(" ")
    """para cada nota en nuestra lista de notas se va a transformar en float. esto es un comprehension"""
    notas =[float(nota)for nota in n]
    return notas
