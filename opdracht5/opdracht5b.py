
import RPi.GPIO as GPIO
# Import de  de tijd module
import time
led = 9
led2 = 12

schakelaar = 10
schakelaar1 =11

# Fysieke pin nummer gebruiken
GPIO.setmode(GPIO.BCM)

# schakelaar
GPIO.setup(schakelaar, GPIO.IN)
# pin 9 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

begin = time.time()
begin2 = time.time()

# schakelaar
GPIO.setup(schakelaar1, GPIO.IN)
# pin 12 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(led2, GPIO.OUT, initial=GPIO.LOW)

while True:
#als je io schakelaar  indruk dan pin9 gaat aan
    if GPIO.input(schakelaar):
        GPIO.output(led, GPIO.HIGH)# aanzetten
        if time.time()-1 > begin:
            GPIO.output(led, GPIO.LOW) # uitzetten
        if time.time() - 2 > begin:
            begin=time.time()

#als je io schakelaar 1 indruk dan pin12 gaat aan
    if GPIO.input(schakelaar1):
        GPIO.output(led2, GPIO.HIGH)# aanzetten
        if time.time()-0.7 > begin:
            GPIO.output(12, GPIO.LOW) # uitzetten
        if time.time() - 1.4 > begin:
            begin=time.time()

    time.sleep(0.1)