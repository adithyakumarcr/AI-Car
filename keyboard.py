#Keypad for KIKI 
import motor

from time import sleep
import time

import sys, select, termios, tty


print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

settings = termios.tcgetattr(sys.stdin)

while(1):

    x= getKey()
    
    if x=='w':
        motor.front()
        time.sleep(0.05)
        motor.stop()
        x='z'


    elif x=='s':
        motor.back()
        time.sleep(0.05)
        motor.stop()
        x='z'

    elif x=='a':
        motor.left()
        time.sleep(0.05)
        motor.stop()
        x='z'

    elif x=='d':
        motor.right()
        time.sleep(0.05)
        motor.stop()
        x='z'

    elif x=='l':
        print("low")
        motor.speedLow()
        x='z'

    elif x=='m':
        print("medium")
        motor.speedMed()
        x='z'

    elif x=='h':
        print("high")
        motor.speedHigh()
        x='z'
     
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    



