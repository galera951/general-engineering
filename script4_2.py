from ledCls import Leds
from time import time, sleep

leds = Leds()
period = 10


try:
    start = time()
    while True:
        val = time() - start
        val %= period
        val -= period / 2 
        val = abs(val)
        leds.push(int(val * 256 / period * 2))
        sleep(0.01)
finally:
    leds.close()