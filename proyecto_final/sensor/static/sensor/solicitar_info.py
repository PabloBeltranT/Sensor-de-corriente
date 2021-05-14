from random import randint, randrange
from sensor.models import Datos_de_consumo
import serial
from time import sleep

from asgiref.sync import sync_to_async

try:
    placa_de_adquisicion = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
    print("Se encontro puerto serie.")
except:
    print("No se encontro puerto serie!!!")

#@sync_to_async
def solicitar():

    #placa_de_adquisicion = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
    #sleep(2)

    placa_de_adquisicion.write(b'a')
    corriente = placa_de_adquisicion.readline()#.decode('ascii')
    corriente = float(corriente)
    #print(format(corriente, ".4f"))
    fuente = 'Solar'

    if corriente < 0.8000:
        #print("utilizando corrinete solar")
        placa_de_adquisicion.write(b'b')
        fuente = 'Solar'
        #sleep(2)

    if corriente > 0.8000:
        #print("utilizando corrinete comercial")
        placa_de_adquisicion.write(b'c')
        fuente = 'comercial'
        #sleep(2)

    #placa_de_adquisicion.close()

    potencia_consumida_solar = 0
    potencia_consumida_comercial = 0
    data = {
        'corriente':corriente,
        'fuente':fuente,
    }
    print('Corriente: ', corriente, '  |  ', 'Utilizando corriente ', fuente)
    return data 



@sync_to_async
def almacenar_info(datos):
    nuevo_dato = Datos_de_consumo(
        fecha = datos['fecha'],
        hora  = datos['hora'],
        corrinete_consimuda_en_directa = datos['corrinete_consimuda_en_directa'],
        potencia_consumida_en_directa  = datos['potencia_consumida_en_directa'],
        timepo_de_consumo_en_red_comercial = datos['timepo_de_consumo_en_red_comercial']
        )
    nuevo_dato.save()
