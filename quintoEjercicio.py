import big_o

def solucion(S):
    '''
    Funcion: solucion, la funcion devuelve el índice (contando desde 0)
             de un carácter tal que la parte de la cadena a la izquierda de ese carácter 
             es una inversión de la parte de la cadena a su derecha.


    Parametros: s

    Retorna: mid
    '''
    #
    sLen = len(S)
    if sLen % 2 == 0:   
        #nops retorna el -1
        return -1
    mitad = sLen // 2
    comienzo, fin = 0, sLen-1

    while comienzo < mitad:
        if S[comienzo] != S[fin]: 
            #nos retorna el -1     
            return -1
        comienzo += 1
        fin -= 1
    #nos retorna la mitad 
    return mitad

if __name__ == '__main__':
    #ingresamos la cadena de caracteres 
    cadena = input(f"Ingrese la cadena: ")
    #nos va a mostar el unico numero que no se repite llamando a la funcion solucion 
    print("El unico numero que no se repite es :",solucion(cadena))