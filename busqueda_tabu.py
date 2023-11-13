import random

def funcion_objetivo(solucion):
    # Define aquí tu función objetivo que debe ser minimizada
    # Esta función debe tomar una solución (una lista de valores) como entrada
    # y devolver un valor que indique la calidad de la solución.

    # En este ejemplo, utilizaremos una función de ejemplo simple.
    return sum(solucion)

def generador_vecindario(solucion):
    # Define aquí cómo generar soluciones vecinas a partir de una solución dada.
    # En este ejemplo, generamos soluciones vecinas cambiando aleatoriamente un elemento.

    vecindario = []
    for i in range(len(solucion)):
        vecino = solucion[:]
        vecino[i] = 1 - vecino[i]  # Cambia el valor 0 a 1 o viceversa
        vecindario.append(vecino)
    return vecindario

def busqueda_tabu(solucion_inicial, iteraciones, tamano_lista_tabu):
    mejor_solucion = solucion_inicial
    mejor_valor = funcion_objetivo(mejor_solucion)
    solucion_actual = solucion_inicial
    lista_tabu = []

    for _ in range(iteraciones):
        vecindario = generador_vecindario(solucion_actual)
        mejor_vecino = None
        mejor_valor_vecino = float('inf')

        for vecino in vecindario:
            valor_vecino = funcion_objetivo(vecino)

            if valor_vecino < mejor_valor_vecino and vecino not in lista_tabu:
                mejor_vecino = vecino
                mejor_valor_vecino = valor_vecino

        if mejor_valor_vecino < mejor_valor:
            mejor_solucion = mejor_vecino
            mejor_valor = mejor_valor_vecino

        solucion_actual = mejor_vecino

        # Agregar la mejor solución a la lista tabú
        lista_tabu.append(mejor_solucion)
        if len(lista_tabu) > tamano_lista_tabu:
            lista_tabu.pop(0)

    return mejor_solucion, mejor_valor

# Ejemplo de uso
solucion_inicial = [0, 1, 0, 1, 0]
iteraciones = 100
tamano_lista_tabu = 5

mejor_solucion, mejor_valor = busqueda_tabu(solucion_inicial, iteraciones, tamano_lista_tabu)

print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la función objetivo:", mejor_valor)
