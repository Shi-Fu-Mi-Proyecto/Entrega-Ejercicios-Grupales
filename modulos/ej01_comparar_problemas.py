'''
Módulo con las funciones relativas al ejercicio 1: 'Compara los Problemas'
'''

# ---------- IMPORTACIONES ----------
import random

# ---------- FUNCIONES ----------

def calif_media_aleat(a):
    '''
    Funcion que dado un numero, devuleve un triplete de numeros aleatorios cuya media es el número dado
    '''
    while True:
        trio = [random.randint(1, 100) for i in range(3)]
        if sum(trio)/3 == a:
            return trio
        else:
            pass

def compareTriplets(a, b):
    '''
    Función que dada la calificación los desafíos de Lucía y Carlos, devuelve la puntuación de cada uno, tras la calificaión del revisor.
    -INPUT -----:
    a: int
        calificación del desafío de Lucía (1-100)
    b: int 
        calificación del desafío de Carlos (1-100)
    -OUTPUT ----:
    (lucia, carlos): tuple
        puntuación de Lucía y puntuacion de Carlos
    '''
    puntos_a = calif_media_aleat(a) #lista de puntos en cada categoría de Lucía
    # print('puntos Lucia',puntos_a)
    puntos_b = calif_media_aleat(b) #lista de puntos en cada categoría de Carlos
    # print('puntos Carlos',puntos_b)
    lucia = 0 # puntuacion de lucia
    carlos = 0  # puntuacion de carlos

    # puntuamos para cada categoría
    for i in range(3): 
        if puntos_a[i] > puntos_b[i]: # Lucia tiene más puntos
            lucia += 1
        elif puntos_a[i] < puntos_b[i]: # Carlos tiene más puntos
            carlos += 1
        elif puntos_a[i] == puntos_b[i]: # tienen los mismos puntos
            pass
    
    return lucia, carlos

def juego_comparacion():
    '''
    Funcion lanzadora del juego
    '''
    a = int(input("Introduce la calificacion de Lucia: "))
    b = int(input("Introduce la calificacion de Carlos: "))
    lucia, carlos = compareTriplets(a, b)
    print("La puntuacion de Lucia es: ", lucia, " y la de Carlos es: ", carlos) 

    if lucia > carlos:
        print("Lucia gana")
    elif lucia < carlos:
        print("Carlos gana")
    elif lucia == carlos:
        print("Empate")



    