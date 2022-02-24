# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# schakelaar
GPIO.setup(16, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(7, GPIO.IN)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

gpiostate = [GPIO.LOW, GPIO.HIGH]

try:
    while True:
        GPIO.output(26, gpiostate[GPIO.input(16)])
        GPIO.output(21, gpiostate[GPIO.input(13)])
        GPIO.output(20, gpiostate[GPIO.input(12)])
        GPIO.output(19, gpiostate[GPIO.input(7)])

finally:
    GPIO.cleanup()