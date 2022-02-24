# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO

import time
led = 8
led2 = 12

schakelaar = 10
schakelaar1 =11

# Fysieke pin nummer gebruiken
GPIO.setmode(GPIO.BCM)

# schakelaar
GPIO.setup(schakelaar, GPIO.IN)

# pin 9 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

begin = time.time()


# schakelaar
GPIO.setup(schakelaar1, GPIO.IN)

# pin 9 in als uitgangspin en  de beginwaarde is uit
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

try:

    while True:

        if GPIO.input(schakelaar):
            print("gele led dennis6")
            if time.time() > begin:
                GPIO.output(led, GPIO.HIGH)
                GPIO.output(led2, GPIO.LOW)
            if time.time() - 1 > begin:
                GPIO.output(led, GPIO.LOW)
                GPIO.output(led2, GPIO.HIGH)
            if time.time() - 2 > begin:
                begin = time.time()

        else:
            if time.time() > begin:
                GPIO.output(led, GPIO.HIGH)
                GPIO.output(led2, GPIO.LOW)
            if  time.time() - 1.3 > begin:
                GPIO.output(led, GPIO.LOW)
                GPIO.output(led2, GPIO.HIGH)
            if time.time() - 2 > begin:
                begin = time.time()

        time.sleep(0.1)
finally:
    GPIO.cleanup()