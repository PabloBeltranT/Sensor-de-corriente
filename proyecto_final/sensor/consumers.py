from sensor.models import Datos_de_consumo
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asyncio import sleep
from .static.sensor.solicitar_info import solicitar, almacenar_info
import datetime
import time
from random import randint, randrange

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        while True:

            data = solicitar()
            corriente = data['corriente']
            fuente = data['fuente']
            await self.send(json.dumps({'message':corriente,
                                        'fuente':fuente
                                        }))
            await almacenar_info(
                datos = {
                    'fecha': datetime.date.today(),
                    'hora': time.time(),
                    'corrinete_consimuda_en_directa': randint(0, 20),
                    'potencia_consumida_en_directa': randint(0, 1000),
                    'timepo_de_consumo_en_red_comercial': randrange(0, 24),
                }
            )
            await sleep(0.1)
