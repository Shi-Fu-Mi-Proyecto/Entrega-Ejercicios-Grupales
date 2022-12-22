'''
Módulo con las funciones relativas al ejercicio 2: 'Naranjas y Manzanas'
'''

# ---------- IMPORTACIONES ----------
import random

# ---------- FUNCIONES ----------

def countApplesAndOranges(s, t, a, b, apples, oranges):
    '''
    Funcion que dadas las entradas pedidas, devuelve la cantidad de manzanas y naranjas que caen en casa de Sam
    -INPUT-----:
    s (int): inicio del segmento de la casa
    t (int): fin del segmento de la casa
    a (int): ubicacion manzano
    b (int): ubicacion naranjo
    apples (int): cantidad de manzanas
    oranges (int): cantidad de naranjas
    -OUTPUT-----:
    (int,int): cantidad de manzanas y naranjas que caen en el segmento de la casa
    '''
    # MANZANAS
    manzanas_en_casa = 0
    for manzana in range(apples): #para cada manzana
        d = random.randint(-(b-a),b-a) # distancia del manzano a la que cae la manzana
        # digamos que la distancia máxima a la que puede caer la manzana es el naranjo
        pos_manzana = a + d # posición global
        # print('posicion manzana:',pos_manzana)
        if pos_manzana >= s and pos_manzana <= t: #si la manzana cae en el segmento de la casa
            manzanas_en_casa += 1  
    else:
        pass
    
    # NARANJAS
    naranjas_en_casa = 0
    for naranja in range(oranges): #para cada naranja
        d = random.randint(-(b-a),b-a) # distancia del naranjo a la que cae la naranja
        # digamos que la distancia máxima a la que puede caer la naranja es el manzano
        pos_naranja = b + d # posición global
        if pos_naranja >= s and pos_naranja <= t: #si la manzana cae en el segmento de la casa
            naranjas_en_casa += 1
        else:
            pass
    
    return (manzanas_en_casa,naranjas_en_casa)


def juego_manzanas_naranjas():
    '''
    Funcion lanzadora del juego
    '''
    print('Según el diagrama del ejercicio:')
    a = int(input('Introduce la posición del manzano: '))
    b = int(input('Introduce la posición del naranjo: '))
    s = int(input('Introduce la posición en la que empiza la casa de Sam: '))
    t = int(input('Introduce la posición en la que termina la casa de Sam: '))
    apples = int(input('Introduce la cantidad de manzanas que van a caer: '))
    oranges = int(input('Introduce la cantidad de naranjas que van a caer: '))

    manzanas_Sam, naranjas_Sam = countApplesAndOranges(s, t, a, b, apples, oranges)
    print('Han caído',manzanas_Sam, 'manzanas en casa de Sam')
    print('Han caído',naranjas_Sam, 'naranjas en casa de Sam')
