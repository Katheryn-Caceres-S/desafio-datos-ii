

def calcular_estadisticas(notas:list[float]) -> dict :
    """calcula las estadisticas de una lista de notas
    promedio
    mayor
    menor
    aprobados
    """

    try: 
        promedio = sum (notas) / len(notas)
        mayor = max(notas)
        menor = min(notas)
        aprobado = [a for a in notas if a >= 4.0]

        resultado = {
            "promedio": promedio,
            "mayor" : mayor,
            "menor": menor,
            "aprobado": aprobado
        }
        return resultado

        """print (promedio)
        print (mayor, menor)
        print (aprobado) """
    except ZeroDivisionError:
        print("no hay notas agregadas")