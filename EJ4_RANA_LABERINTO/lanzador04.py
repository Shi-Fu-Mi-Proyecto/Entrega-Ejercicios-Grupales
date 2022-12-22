# ---------- IMPORTACIONES ----------
from data04.lab import laberinto_inicial
from modulos04.movimientos import imprimir_laberinto, moverse_a_celda_adyacente

# ---------- VARIABLES ----------
MOVIMIENTOS = [] #lista donde vamos a ir guardando los movimientos que hace la rana

# ---------- FUNCIONES ----------

def guardar_laberinto(laberinto):
    '''
    Guarda el tablero en el archivo historial_movimientos.txt
    '''
    with open("EJ4_RANA_LABERINTO\data04\historial_movimientos.txt", "a", encoding="utf-8") as archivo:
        for fila in laberinto:
            lista_texto = [] # lista para guardar el texto de cada fila
            for columna in fila:
                lista_texto.append(columna)
                lista_texto.append(' ') # añadimos un espacio entre cada columna
            archivo.writelines(lista_texto) # escribimos la lista en el archivo
            archivo.writelines('\n') # salto de línea para la siguiente fila de texto
            
        archivo.writelines('\n') # salto de línea para la siguiente fila de texto
        archivo.close()


def jugar_rana_laberinto():
    '''
    Función que lanza el juego de la rana en el laberinto
    '''
    print('¡Bienvenido al juego de la rana en el laberinto!')
    print()
    print('Este es el laberinto en el que se encuentra la rana Alef:')
    imprimir_laberinto(laberinto_inicial)

    laberinto = laberinto_inicial
    while True:
        guardar_laberinto(laberinto) # guardamos el laberinto en el archivo externo
        laberinto = moverse_a_celda_adyacente(laberinto)

        if laberinto[4][3]=='A' or laberinto[4][7]=='A' or laberinto[4][8]=='A': # si pisa una bomba
            print('Alef ha pisado una bomba y ha muerto. ¡Has perdido!')
            break #se acaba el juego

        if laberinto[-1][1]=='A' or laberinto[-1][5]=='A':
            print('Alef ha conseguido llegar a la salida. ¡Has ganado!')
            break

    print('Alef ha realizado',len(MOVIMIENTOS),'movimientos:')
    print(MOVIMIENTOS)

