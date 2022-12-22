'''
Módulo con las funciones relativas al ejercicio 1: 'Compara los Problemas'
'''

def compareTriplets(a, b):
    '''
    Función que dada la calificación media de Lucía y Carlos, devuelve la puntuación de cada uno.
    -INPUT -----:
    a: list
        lista de calificaciones de Lucía en las 3 categorías
    b: list 
        lista de calificaciones de Carlos en las 3 categorías
    -OUTPUT ----:
    (lucia, carlos): tuple
        puntuación de Lucía y puntuacion de Carlos
    ''' 
    lucia = 0 # puntuacion de lucia
    carlos = 0  # puntuacion de carlos

    # puntuamos para cada categoría
    for i in range(3): 
        if a[i] > b[i]: # Lucia tiene más puntos
            lucia += 1
        elif a[i] < b[i]: # Carlos tiene más puntos
            carlos += 1
        elif a[i] == b[i]: # tienen los mismos puntos
            pass
    
    return lucia, carlos


def juego_comparacion():
    valores_a = input('Introduce las calificaciones de Lucia en las 3 categorías (separadas por espacios): ')
    valores_b = input('Introduce las calificaciones de Carlos en las 3 categorías (separadas por espacios): ')
    a = list(map(int, valores_a.split()))
    b = list(map(int, valores_b.split()))
    lucia, carlos = compareTriplets(a, b)
    print("La puntuacion de Lucia es:", lucia, ", y la de Carlos es:", carlos) 
    
    # indicamos el ganador
    if lucia > carlos:
        print("Lucia gana")
    elif lucia < carlos:
        print("Carlos gana")
    elif lucia == carlos:
        print("Empate")