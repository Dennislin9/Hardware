
import RPi.GPIO as GPIO
# Import de slaap functie voor de tijd module
from time import sleep

button1 = 8
button2 = 15

GPIO.setwarnings(False)
#Fysieke pin nummer gebruiken
GPIO.setmode(GPIO.BCM)
#pin 9 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(button1, GPIO.OUT, initial=GPIO.LOW)
#pin 15 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(button2, GPIO.OUT, initial=GPIO.LOW)

while True:

 GPIO.output(button1, GPIO.HIGH) # aanzetten
 sleep(1.3)  # wacht 1.3 seconde
 GPIO.output(button1, GPIO.LOW) # uitzetten
 sleep(0.7) # wacht 0.7 seconde

 GPIO.output(button2, GPIO.LOW) # aanzetten
 sleep(0.8)  # wacht 0.8 seconde
 GPIO.output(button2, GPIO.HIGH) # uitzetten
 sleep(1.7)# wacht 1.7 seconde

