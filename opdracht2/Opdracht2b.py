#Raspberry Pi GPIO-bibliotheek importeren
import RPi.GPIO as GPIO
# Importeer de slaapfunctie uit de tijdmodule
from time import sleep

GPIO.setwarnings(False)
#Fysieke pin nummer gebruiken
GPIO.setmode(GPIO.BCM)
#pin 8 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(9, GPIO.OUT, initial=GPIO.HIGH)

while True:
 GPIO.output(9, GPIO.LOW) # aanzetten
 sleep(1) # wacht 1 sec
 GPIO.output(9, GPIO.HIGH) # uitzetten
 sleep(2) # wacht 2 seconde