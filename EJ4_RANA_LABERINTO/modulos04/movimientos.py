# ---------- IMPORTACIONES ----------
from data04.lab import laberinto_inicial
import random

# ---------- VARIABLES ----------
MOVIMIENTOS = [] #lista donde vamos a ir guardando los movimientos que hace la rana

# ---------- FUNCIONES ----------
def imprimir_laberinto(laberinto):
    '''
    Función que impreme el laberinto en pantalla
    '''
    for fila in laberinto:
        for celda in fila:
            print(celda, end=' ')
        print()


def comprobar_celda_vacia(laberinto, fila, columna):
    '''
    Función que comprueba si una celda está vacía
    '''
    if laberinto[fila][columna] == ' ':
        return True
    else:
        return False

# CASILLAS ESPECIALES

def tunel_1(lab, f, c): # posicion rana (f,c)
    if (f,c) == (1,3):
        lab[5][1] = 'A' # la rana se va al otro extremo del túnel
        lab[f][c] = 'o'
        return lab
    elif (f,c) == (5,1):
        lab[1][3] = 'A' # la rana se va al otro extremo del túnel
        lab[f][c] = 'o'
        return lab
    
def tunel_2(lab, f, c): # posicion rana (f,c)
    if (f,c) == (1,5):
        lab[3][5] = 'A' # la rana se va al otro extremo del túnel
        lab[f][c] = 'O'
        return lab
    elif (f,c) == (3,5):
        lab[1][5] = 'A' # la rana se va al otro extremo del túnel
        lab[f][c] = 'O'
        return lab

def reemplazar_en_caso_tunel(lab, pos_inicial, pos_final):
    f_0, c_0 = pos_inicial
    f_1, c_1 = pos_final
    
    if (f_0,c_0) == (1,3) or (f_0,c_0) == (5,1): # si la casilla en la que estamos hay un túnel de tipo 1
        lab[f_1][c_1] = 'A' # movemos la rana a la nueva casilla
        lab[f_0][c_0] = 'o' # dejamos la otra de tipo tunel 1
        return lab
    
    elif (f_0,c_0) == (1,5) or (f_0,c_0) == (3,5): # si en la casilla en la que estamos hay un túnel de tipo 2
        lab[f_1][c_1] = 'A' # movemos la rana a la nueva casilla
        lab[f_0][c_0] = 'O' # dejamos la otra de tipo tunel 2
        return lab


# MOVERSE
def mov_segun_tipo_celda(lab, pos_inicial, pos_final):
    f_0, c_0 = pos_inicial
    f_1, c_1 = pos_final
    
    # CELDA VACÍA
    if lab[f_1][c_1] == ' ': # si en la casilla donde vamos hay una casilla vacia
        
        if lab[f_0][c_0] == 'o' or lab[f_0][c_0] == 'O': # si la rana acaba de salir de un túnel
            reemplazar_en_caso_tunel(lab, pos_inicial, pos_final)
        
        else: 
            lab[f_1][c_1] = 'A' # movemos la rana a la casilla
            lab[f_0][c_0] = ' ' # dejamos la otra vacia
            return lab
    
    # BOMBA
    elif lab[f_1][c_1] == 'x': # si en la casilla donde vamos hay una bomba
        lab[f_1][c_1] = 'A' # movemos la rana a la casilla
        lab[f_0][c_0] = ' ' # dejamos la otra vacia
        #print('La rana ha muerto por una bomba. Fin del juego.')
        #sys.exit(0) # la rana muere
    
    # TÚNEL TIPO 1
    elif (f_1,c_1) == (1,3) or (f_1,c_1) == (5,1): # si en la casilla donde vamos hay un túnel de tipo 1
        lab[f_1][c_1] = 'A' # movemos la rana a la casilla
        lab[f_0][c_0] = ' ' # dejamos la otra vacia
        return tunel_1(lab, f_1, c_1) # la rana se va al otro extremo del túnel 1
    
    # TÚNEL TIPO 2
    elif (f_1,c_1) == (1,5) or (f_1,c_1) == (3,5): # si en la casilla donde vamos hay un túnel de tipo 2
        lab[f_1][c_1] = 'A' # movemos la rana a la casilla
        lab[f_0][c_0] = ' ' #3 dejamos la otra vacia
        return tunel_2(lab, f_1, c_1) # la rana se va al otro extremo del túnel 2
    
    # SALIDA
    elif lab[f_1][c_1] == 'E': # si en la casilla donde vamos hay una casilla especial
        lab[f_1][c_1] = 'A' # movemos la rana a la casilla
        lab[f_0][c_0] = ' ' # dejamos la otra vacia
        return lab


def moverse_a_celda_adyacente(lab):
    '''
    Funcion que hace que la rana se mueva a una celda vacía adyacente
    -INPUT-----
    lab: list
        laberinto
    f: int
        fila de la posicion en la que se encuntra la rana
    c: int
        columna de la posicion en la que se encuntra la rana
    -OUTPUT-----
    lab: list
        laberinto con la rana movida a una celda vacía adyacente
    '''
    for f in range(len(lab)):
        for c in range(len(lab[f])):
            
            if lab[f][c] == 'A': # la rana está en la casilla (f,c)
                p = random.randint(1,4) # la rana se mueve aleatoriamente a una celda adyacente
                            
                # puede moverse a la celda SUPERIOR
                if p == 1 and lab[f-1][c]!='#': # si la celda superior no es una pared
                    MOVIMIENTOS.append('arriba')
                    return mov_segun_tipo_celda(lab, (f,c), (f-1,c))

                # puede moverse a la celda INFERIOR
                elif p == 2 and lab[f+1][c]!='#': # si la celda inferior no es una pared
                    MOVIMIENTOS.append('abajo')
                    return mov_segun_tipo_celda(lab, (f,c), (f+1,c))

                # puede moverse a la celda de la IZQUIERDA
                elif p == 3 and lab[f][c-1]!='#':  # si la celda de la izquierda no es una pared
                    MOVIMIENTOS.append('izquierda')
                    return mov_segun_tipo_celda(lab, (f,c), (f,c-1))

                # puede moverse a la celda de la DERECHA
                elif p == 4 and lab[f][c+1]!='#':  # si la celda de la derecha no es una pared
                    MOVIMIENTOS.append('derecha')
                    return mov_segun_tipo_celda(lab, (f,c), (f,c+1))
                
            else:
                pass 

