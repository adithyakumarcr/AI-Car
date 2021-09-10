# Python Script
import RPi.GPIO as GPIO          

enA = 33
enB = 32
in1 = 35
in2 = 37
in3 = 29
in4 = 31
in5 = 11
in6 = 13
in7 = 19
in8 = 21


temp1=1

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)

GPIO.setup(in1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in2,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(in5,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in6,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(in3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in4,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(in7,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in8,GPIO.OUT,initial=GPIO.LOW)

pwmA=GPIO.PWM(enA,100)
pwmB=GPIO.PWM(enB,100)

pwmA.start(20)
pwmB.start(20)

pwmA.ChangeDutyCycle(100)
pwmB.ChangeDutyCycle(100)


	
def front():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)

    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
         
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.HIGH)

    GPIO.output(in7,GPIO.HIGH)
    GPIO.output(in8,GPIO.LOW)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
        
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.LOW)

    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.LOW)

def back():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
         
    GPIO.output(in5,GPIO.HIGH)
    GPIO.output(in6,GPIO.LOW)

    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.HIGH)

def left():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)

    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

    GPIO.output(in5,GPIO.HIGH)
    GPIO.output(in6,GPIO.LOW)

    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.HIGH)

def right():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.HIGH)

    GPIO.output(in7,GPIO.HIGH)
    GPIO.output(in8,GPIO.LOW)

def speedLow():
    pwmA.ChangeDutyCycle(100)
    pwmB.ChangeDutyCycle(100)
def speedHigh():
    pwmA.ChangeDutyCycle(50)
    pwmB.ChangeDutyCycle(50)

