import RPi.GPIO as GPIO
from requestsAPI import *
import url 
import time

class ultraSonicoHRSR01: 
    '''
    ¿Que propiedades y metodos tienen estos objetos?
    PENSAR EN MODO MANUAL Y AUTOMATICO 
    '''
    def __init__(self, echo, trig, endpoint, prefix):
        self.echo = echo 
        self.trig = trig
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.setup(self.trig, GPIO.OUT)
        self.objResponse = requestsAPI(endpoint, prefix)

    def calcularDistancia(self) -> float: 
        GPIO.output(self.trig, GPIO.LOW)
        time.sleep(0.1)

        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trig, GPIO.LOW)

        while True:
            pulso_inicio = time.time()
            if GPIO.input(self.echo) == GPIO.HIGH:
                break

        while True:
            pulso_fin = time.time()
            if GPIO.input(self.echo) == GPIO.LOW:
                break

        duracion = pulso_fin - pulso_inicio
        distancia = (34300 * duracion) / 2
        return distancia