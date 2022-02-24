# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# schakelaar
GPIO.setup(26, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.IN)


GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

gpiostate = [GPIO.LOW, GPIO.HIGH]

try:
    while True:
        GPIO.output(19, gpiostate[GPIO.input(26)])
        GPIO.output(16, gpiostate[GPIO.input(21)])
        GPIO.output(13, gpiostate[GPIO.input(20)])

finally:
    GPIO.cleanup()