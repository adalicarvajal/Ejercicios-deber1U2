import big_o

def max_power_of_2(n):
    '''
    Funcion: La funcion max_power sirve para encontrar la potencia mas alta

    Parametros:n

    Retorna:max_power
    '''
    #inicializamos el max_power con 0 para que no guarde ningun archivo basura(no es obligatorio hacerlo)
    max_power = 0
    #creamos el while con el n(numero)
    while n:
        n = n & (n - 1)
        max_power += 1
    #aqui nos retorna la potencia mas alta del numero ingresado
    return max_power
if __name__ == '__main__':
    # ingresamos el numero 
    n = int(input("Ingrese un número: "))
    #llamamos a la funcion para retornar ;a potencia mas alta del numero ingresado
    print(max_power_of_2(n))
    positive_int_generator = lambda n: n
    best, others= big_o.big_o(max_power_of_2,positive_int_generator)
    print(best)