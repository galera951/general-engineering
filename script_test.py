import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

t = np.linspace(0.0005, 0.02, 60)

while True:
    for i in t:
        GPIO.output(26, 1)
        time.sleep(i)
        GPIO.output(26, 0)
        time.sleep(.01)