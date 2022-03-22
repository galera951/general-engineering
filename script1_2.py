import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

signal = 1
print(signal)

#111
GPIO.output(26, signal)

time.sleep(1)

GPIO.output(26, 0)

time.sleep(1)

#111
GPIO.output(26, signal)

time.sleep(1)

GPIO.output(26, 0)

time.sleep(1)

#111
GPIO.output(26, signal)

time.sleep(1)

GPIO.output(26, 0)

time.sleep(1)

