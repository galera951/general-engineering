import RPi.GPIO as GPIO
import time
#import numpy as np

pins = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)


def start_program():
    for pin in pins:
        GPIO.output(pin, 1)
        time.sleep(0.2)
        GPIO.output(pin, 0)
    GPIO.output(pins, 0)

if __name__ == "__main__":
    for _ in range(3):
        start_program()
    GPIO.cleanup()