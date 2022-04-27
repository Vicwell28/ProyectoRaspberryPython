import RPi.GPIO as GPIO
import time
from led import *
from L298N import *
import requestsAPI as api
import url
from fc21 import *
from hrsr01 import *
import json

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ESPERA = 0.5; 

apiC = api.requestsAPI(url.urlEndpoint, url.urlPrefix)
apiC.obtenerToken(url.urlCredenciales)

led = ledclass(31, url.urlEndpoint, url.urlPrefix)
controladorMotor = ControladorL298N(url.urlEndpoint, url.urlPrefix, 11, 12, 13, 15, 16, 18)
infrarrojoDerecho  = infrarrojofc21(url.urlEndpoint, url.urlPrefix, 38, apiC.token)
infrarrojoIzquierdo  = infrarrojofc21(url.urlEndpoint, url.urlPrefix, 40, apiC.token)
ultrasonicoDelantero = ultraSonicoHRSR01(35, 37, url.urlEndpoint, url.urlPrefix)
ultrasonicoTrasero = ultraSonicoHRSR01(23, 24, url.urlEndpoint, url.urlPrefix)
print("Modificado desde github.com")
print("Conecando...")

DATAINFRARROJODERECHA = 0; 
DATAINFRARROJOIZQUIERDO = 0; 
DATATEMPERATURA = 0; 
DATAULTRASONICODELANTERO = 0;  
DATAULTRASONICOTRASERO = 0; 
DATAVELOCIDAD = 0; 

while True:
    print("Consumiendo...")
    DATAULTRASONICODELANTERO = ultrasonicoDelantero.calcularDistancia()
    print(DATAULTRASONICODELANTERO)
    DATAULTRASONICOTRASERO = ultrasonicoTrasero.calcularDistancia()
    print(DATAULTRASONICOTRASERO)
    DATAINFRARROJODERECHA = infrarrojoDerecho.detectarObstaculo()
    print(DATAINFRARROJODERECHA)
    DATAINFRARROJOIZQUIERDO = infrarrojoIzquierdo.detectarObstaculo()
    print(DATAINFRARROJOIZQUIERDO)
    
    
    res = apiC.postStore(url.urldataAuto,url.urlgetMoviemiento)['movimiento'][0]
    apiLed = apiC.postStore(url.urldataAuto, url.urlgetLed)['estado'][0]['estado']
    print(res)
    print(apiLed)
    
    if apiLed:
        led.encenderLed()
    else:
        led.apagarLed(); 
    
    if res['Motor_Delante']:
        if DATAULTRASONICODELANTERO <= 10.00:
            controladorMotor.MotorApagado()
        else:  
            controladorMotor.MotorDelante(res['Motor_Velocidad'])
        
    elif res['Motor_Reversa']: 
        if DATAULTRASONICOTRASERO <= 10.00: 
            controladorMotor.MotorApagado()
        else: 
            controladorMotor.MotorReversa(res['Motor_Velocidad'])
        
    elif res['Motor_Derecha']:
        DATAINFRARROJODERECHA = infrarrojoDerecho.detectarObstaculo()
        if DATAINFRARROJODERECHA:
            print("No hay objectos a la derecha")
            controladorMotor.MotorDerecha(res['Motor_Velocidad'])
        else: 
            print("Detecto un objeto")
            controladorMotor.MotorApagado()

        
    elif res['Motor_Izquierda']:
        DATAINFRARROJOIZQUIERDO = infrarrojoIzquierdo.detectarObstaculo()
        if DATAINFRARROJOIZQUIERDO:
            print("No hay obstaculos en la izqueirda")
            controladorMotor.MotorIzquierda(res['Motor_Velocidad'])
        else: 
            print("Hay obstaculos enfrente")
            controladorMotor.MotorApagado()
        
    elif res['Motor_Apagado']:
        controladorMotor.MotorApagado()
    
    enviarData = {
	"auto" : url.urldataAuto['auto'],
	"valores":{
            'temperatura':{
                "valor":100
            },
            "ultrasonico1":{
                "valor": DATAULTRASONICODELANTERO
            },
            "ultrasonico2":{
                "valor": DATAULTRASONICOTRASERO
            },
            "velocidad":{
                "valor": res['Motor_Velocidad']
            },
            "infrarrojo2":{
                "valor": DATAINFRARROJODERECHA
            }, 
            "infrarrojo1":{
                "valor": DATAINFRARROJOIZQUIERDO
            }
	    }
    }

    apiC.postStore(enviarData, url.urlSetValores)
    time.sleep(ESPERA)
    
GPIO.cleanup()
