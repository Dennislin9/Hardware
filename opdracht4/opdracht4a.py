
import RPi.GPIO as GPIO
# Import de  de tijd module
import time
button1 = 8
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
        print("denius ")
        GPIO.output(button1, GPIO.HIGH)
#anders gaat het uit
    else:
        GPIO.output(button1, GPIO.LOW)
    time.sleep(0.1)