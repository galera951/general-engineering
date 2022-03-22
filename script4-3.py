import RPi.GPIO as GPIO
from time import time, sleep

a = 50
frequency = 50

out_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(out_pin, GPIO.OUT)


try:
    start = time()
    while True:
        if ((start - time()) % (1 / frequency)) < (1 / frequency) * (a / 100):
            GPIO.output(out_pin, 1)
        else:
            GPIO.output(out_pin, 0)
finally:
    GPIO.cleanup()