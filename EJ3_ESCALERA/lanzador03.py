# Módulo con las funciones del ejercicio 3: 'Escalera'

def escalera(n):
    '''
    Función que dibuja la escalera de n pisos
    '''
    for i in range(1, n+1):
        return"\n".join([" "*(n-i) + " #"*i for i in range(1, n+1)])
