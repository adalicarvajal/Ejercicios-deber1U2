import big_o

def solucion(lst):
    '''
    Funcion: solucion, Se da una matriz lst no vacía que consta de N enteros

    Parametros: lst

    Retorna: -1

    '''
    counts = {}
   #Este for lo hacemos para crear la matriz 
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    #Este for va a recorrer la matriz
    for item in lst:
        if counts[item] == 1:
            return item
    #retornamos el -1
    return -1
if __name__ == "__main__":
    numeros = []
    cantidad = int(input(f"Cantidad de numeros a ingresar: "))
    for i in range(cantidad):
        # Recuerda que range comenzara desde 0, asi que imprimimos el numero solicitado pero + 1
        numero = input(f"Ingresa el numero {i + 1}: ")
        # Convertir a entero, pues input regresa una cadena
        numero = int(numero)
        # Lo agregamos al arreglo con append
        numeros.append(numero)

    print("El unico numero que no se repite es :",solucion(numeros))

    positive_int_generator = lambda n: numero
    best, others= big_o.big_o(solucion,positive_int_generator)
    print(best)