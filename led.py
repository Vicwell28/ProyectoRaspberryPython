from requestsAPI import *
import url 
import RPi.GPIO as GPIO

class ledclass: 
    '''
    ¿Que propiedades y metodos tienen estos objetos?
    PENSAR EN MODO MANUAL Y AUTOMATICO 
    '''
    def __init__(self, pin, endpoint, prefix):
        self.status = 0; 
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.objResponse = requestsAPI(endpoint, prefix)

    def getStatusLed(self, data, path) -> bool: 
        response = self.objResponse.postStore(data, path)
        return response['estado'][0]['estado']

    def encenderLed(self) -> None: 
        GPIO.output(self.pin, GPIO.HIGH)
    
    def apagarLed(self) -> None:
        GPIO.output(self.pin, GPIO.LOW)



