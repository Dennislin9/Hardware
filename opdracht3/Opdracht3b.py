
import RPi.GPIO as GPIO
# Import de slaap functie voor de tijd module
from time import sleep
button1 = 8
button2 = 15
#import GPIO as GPIO

GPIO.setwarnings(False)
#Fysieke pin nummer gebruiken
GPIO.setmode(GPIO.BCM)
#pin 9 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(button1, GPIO.OUT, initial=GPIO.LOW)
#pin 15 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(button2, GPIO.OUT, initial=GPIO.LOW)

while True: # Run forever

 GPIO.output(8, GPIO.HIGH) # aanzetten
 GPIO.output(15, GPIO.LOW) # uitzetten
 sleep(1) # Sleep for 1 second

 GPIO.output(8, GPIO.LOW) # uitzetten
 GPIO.output(15, GPIO.HIGH) # aanzetten
 sleep(1) # Sleep for 1 second

