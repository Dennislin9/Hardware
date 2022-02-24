
import RPi.GPIO as GPIO
# Import de  de tijd module
import time

button1 = 8
button2 = 12

servomotor = 5

GPIO.setmode(GPIO.BCM)
# schakelaar
GPIO.setup(button1, GPIO.IN)
# schakelaar
GPIO.setup(button2, GPIO.IN)
#servomotor
GPIO.setup(servomotor, GPIO.OUT)
#servomoter pwm instelling
pwm = GPIO.PWM(servomotor, 50)
pwm.start(0)
hoek = 0

def SetAngle(angle):
    duty = angle / 18 + 2.5
    pwm.ChangeDutyCycle(duty)


x = 0
while True:
    langzaam = GPIO.input(button2)
    snel = GPIO.input(button1)
    if langzaam or snel:
        print("langzaam " + str(langzaam))
        print("snel " + str(snel))
        while draaien < 120:
            SetAngle(draaien)
            time.sleep(0.1)
            if GPIO.input(button2):
                time.sleep(0.1)
            draaien = draaien + 30
            print(draaien)
        while draaien > 0:
            SetAngle(draaien)
            time.sleep(0.1)
            if GPIO.input(button1):
                time.sleep(0.1)

            draaien = draaien - 30
            print(draaien)