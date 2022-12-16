# ---------- IMPORTACIONES ----------
import math
import os
import random
import re
import sys
#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
# 1. INTEGER s
# 2. INTEGER t
# 3. INTEGER a
# 4. INTEGER b
# 5. INTEGER_ARRAY apples
# 6. INTEGER_ARRAY oranges
#


def countApplesAndOranges(s, t, a, b, apples, oranges):
    '''
    -INPUT:
    s (int): inicio del segmento de la casa
    t (int): fin del segmento de la casa
    a (int): ubicacion manzano
    b (int): ubicacion naranjo
    '''
    # MANZANAS
    manzanas_en_casa = 0
    for manzana in range(apples): #para cada manzana
        d = random.randint(-(b-a),b-a) # distancia del manzano a la que cae la manzana
        # digamos que la distancia máxima a la que puede caer la manzana es el naranjo
        pos_manzana = a + d # posición global
        print('posicion manzana:',pos_manzana)
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



# ---------- PROGRAMA PRINCIPAL
   

