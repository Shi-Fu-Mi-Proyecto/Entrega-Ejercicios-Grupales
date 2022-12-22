'''
Módulo con las funciones del ejercicio 3: 'Escalera'
'''

def escalera(n):
    '''
    Función que dibuja la escalera de n pisos
    '''
    for i in range(1, n+1):
        return"\n".join([" "*(n-i) + " #"*i for i in range(1, n+1)])

def dibujo_escalera():
    '''
    Función que pide el número de pisos para la escalera
    '''
    altura = int(input("Introduce el número de pisos de la escalera: "))
    print(escalera(altura))
