import RPi.GPIO as GPIO
from requestsAPI import *


class infrarrojofc21: 
    
    def __init__(self, endpoint, prefix, pin, token) -> None: 
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)
        self.objResponse = requestsAPI(endpoint, prefix)
        self.objResponse.token = token
        
    def detectarObstaculo(self) -> bool: 
        return GPIO.input(self.pin)
