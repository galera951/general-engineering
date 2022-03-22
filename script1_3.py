import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

signal = GPIO.input(6)
print(signal)

GPIO.output(26, signal)