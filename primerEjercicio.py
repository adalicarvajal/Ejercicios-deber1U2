from datetime import datetime
import big_o
def calcular_tarifa_de_estacionamiento(hora_de_entrada, hora_de_salida):
    '''
    Funcion: La funcion calcular tarifa esta hecha para hacer todos los calculos que nos pide el 
             ejercicio 

    Parametros: hora_de_entrada, hora_de_salida

    Retorna: tarifa 
    '''
    # Convertir las cadenas de tiempo a objetos datetime
    hora_de_entrada = datetime.strptime(hora_de_entrada, "%H:%M")
    hora_de_salida = datetime.strptime(hora_de_salida, "%H:%M")
    
    # Calcular la duración del estacionamiento
    duración_estacionamiento = hora_de_salida - hora_de_entrada
    duración_estacionamiento = int(duración_estacionamiento.total_seconds() / 3600)

    # Aplicar las reglas de facturación
    tarifa = 2
    if duración_estacionamiento > 0:
        tarifa += 3
        tarifa += min(duración_estacionamiento*4, 0) 
    #retorna la tarifa calculada
    return tarifa

if __name__ == '__main__':
    tarifa=[]
    #aqui hacemos el ingreso de la hora que ingreso 
    hora_de_entrada = input("Ingrese la hora de entrada (HH:MM): ")
    #aqui se ingresa la hora en la que sale
    hora_de_salida = input("Ingrese la hora de salida (HH:MM): ")
    #llamamos a la funcion de calcular la tarifa
    tarifa = calcular_tarifa_de_estacionamiento(hora_de_entrada, hora_de_salida)
    #mostramos en pantalla la tarifa que tiene que pagar 
    print(f"La tarifa de estacionamiento es de {tarifa} $")

    positive_int_generator = lambda n: tarifa
    best, others= big_o.big_o(calcular_tarifa_de_estacionamiento,positive_int_generator)
    print(best)