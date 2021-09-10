# Python Script

import RPi.GPIO as GPIO          
from time import sleep
import time


import sys, select, termios, tty


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

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

pwmA.ChangeDutyCycle(100)
pwmB.ChangeDutyCycle(100)


def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


	
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


settings = termios.tcgetattr(sys.stdin)

while(1):

    x= getKey()
    
    if x=='w':
        front()
        time.sleep(0.05)
        stop()
        x='z'


    elif x=='s':
        back()
        time.sleep(0.05)
        stop()
        x='z'

    elif x=='a':
        left()
        time.sleep(0.05)
        stop()
        x='z'

    elif x=='d':
        right()
        time.sleep(0.05)
        stop()
        x='z'

    elif x=='l':
        print("low")
        pwmA.ChangeDutyCycle(25)
        pwmB.ChangeDutyCycle(25)

        x='z'

    elif x=='m':
        print("medium")
        pwmA.ChangeDutyCycle(50)
        pwmB.ChangeDutyCycle(50)

        x='z'

    elif x=='h':
        print("high")
        pwmA.ChangeDutyCycle(75)
        pwmB.ChangeDutyCycle(75)

        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    



