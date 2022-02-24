
import RPi.GPIO as GPIO
# Import de  de tijd module
import time

GPIO.setmode(GPIO.BCM)

shakelaar = 10
shakelaar2 = 11

gpioPins = [2, 3, 4 ,17]




for i in gpioPins:
    GPIO.setup(i, GPIO.OUT)

# schakelaar
GPIO.setup(shakelaar, GPIO.IN)
# schakelaar
GPIO.setup(shakelaar2, GPIO.IN)

setting = 0
wait = (5 - 0.0) / 4096
wait2 = (12 - 0.0) / 4096
timer = 0

try:
    while True:
        while GPIO.input(shakelaar):
            print("shakelaar")
            for i in range(0, 4):
                for x in gpioPins:
                    GPIO.output(x, GPIO.LOW)
                    GPIO.output(gpioPins[i], GPIO.HIGH)
                    timer = time.perf_counter()
                while timer + wait > time.perf_counter():
                    pass
                GPIO.output(gpioPins[(i + 1) % 4], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + wait > time.perf_counter():
                    pass
        while GPIO.input(shakelaar2):
            print("shakelaar2")
            for i in range(3, -1, -1):
                for x in gpioPins:
                    GPIO.output(x, GPIO.LOW)
                GPIO.output(gpioPins[i], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + wait2 > time.perf_counter():
                    pass
                GPIO.output(gpioPins[(i - 1) % 4], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + wait2 > time.perf_counter():
                    pass
        for x in gpioPins:
            GPIO.output(x, GPIO.LOW)
finally:
    GPIO.cleanup()

