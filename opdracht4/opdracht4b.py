
import RPi.GPIO as GPIO
# Import de  de tijd module
import time
button1 = 9
button2 = 10

# Fysieke pin nummer gebruiken
GPIO.setmode(GPIO.BCM)

# schakelaar
GPIO.setup(button2, GPIO.IN)
# pin 9 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(button1, GPIO.OUT, initial=GPIO.LOW)

while True:
#als je io schakelaar 10 indruk dan pin9 gaat aan
    if GPIO.input(button2):

        GPIO.output(button1, GPIO.HIGH)# aanzetten
        time.sleep(1) # Sleep for 1 second
        GPIO.output(button1, GPIO.LOW) # uitzetten
        time.sleep(1) # Sleep for 1 second

    time.sleep(0.1)