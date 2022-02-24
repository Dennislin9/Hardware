# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
knop1 = 10
knop2 = 12

# schakelaar
GPIO.setup(knop1, GPIO.OUT)
# schakelaar
GPIO.setup(knop2, GPIO.IN)

tijd = 0
tijd2 = 0
gpiostate = [GPIO.HIGH, GPIO.LOW]
gpio = 0
gpio2 = 0

try:
    while True:
        if gpio2 == 1:
            gpio2 = GPIO.input(3)

        if GPIO.input(3) != gpio2:
            GPIO.output(2, gpiostate[gpio % 2])
            gpio += 1
            gpio2 = 1

finally:
    GPIO.cleanup()