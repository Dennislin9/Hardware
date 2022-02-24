
import RPi.GPIO as GPIO
# Import de  de tijd module
import time
button1 = 8
button2 = 10

schakelaar = 11
schakelaar1 =12

# Fysieke pin nummer gebruiken
GPIO.setmode(GPIO.BCM)

# schakelaar
GPIO.setup(button2, GPIO.IN)
# pin 9 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(button1, GPIO.OUT, initial=GPIO.LOW)

begin = time.time()
begin2 = time.time()

# schakelaar
GPIO.setup(schakelaar, GPIO.IN)
# pin 9 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(schakelaar1, GPIO.OUT, initial=GPIO.LOW)

while True:
#als je io schakelaar 10 indruk dan pin9 gaat aan
    if GPIO.input(button2):
        GPIO.output(button1, GPIO.HIGH)# aanzetten
        if time.time()-1 > begin:
            GPIO.output(button1, GPIO.LOW) # uitzetten
        if time.time() - 2 > begin:
            begin=time.time()

    time.sleep(0.1)