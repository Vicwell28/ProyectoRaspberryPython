from requestsAPI import *
import url 
import RPi.GPIO as GPIO

class ControladorL298N: 
    
    def __init__(self, endpoint, prefix, ena, in1, in2, in3, in4, enb): 
        self.ENA = ena
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4
        self.ENB = enb
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        self.pwm_ENA=GPIO.PWM(self.ENA,80)
        self.pwm_ENA.start(90)
        self.pwm_ENB=GPIO.PWM(self.ENB,80)
        self.pwm_ENB.start(90)
        self.objResponse = requestsAPI(endpoint, prefix)
        
        
    def MotorDelante(self, velocidad):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        self.pwm_ENA.ChangeDutyCycle(velocidad)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.pwm_ENB.ChangeDutyCycle(velocidad)
    
    def MotorReversa(self, velocidad):
        GPIO.output(self.IN1, GPIO.HIGH)
        self.pwm_ENA.ChangeDutyCycle(velocidad)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        self.pwm_ENB.ChangeDutyCycle(velocidad)
        GPIO.output(self.IN4, GPIO.LOW)
    
    def MotorDerecha(self, velocidad):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.pwm_ENA.ChangeDutyCycle(velocidad)
    
    def MotorIzquierda(self, velocidad):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        self.pwm_ENA.ChangeDutyCycle(velocidad)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
    
    def MotorApagado(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)