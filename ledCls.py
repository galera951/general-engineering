import RPi.GPIO as GPIO

def dec2bin(number):
    return [int(bit) for bit in bin(number)[2:].zfill(8)]


def isfloat(value):
    try:
        if float(value) == int(value):
            return False
        return True
    except ValueError:
        return False


class Leds:
    def __init__(self):
        self.pins = [10, 9, 11, 5, 6, 13, 19, 26][::-1]

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pins, GPIO.OUT)

    def push(self, value, out=False):
        value = str(value)
        
        if isfloat(value):
            print("Entered value is not a integer!")

        elif not value.isdigit():
            print("Entered value is NaN!")

        else:
            if int(value) < 0:
                print("Entered value is negative!")
            elif int(value) > 255:
                print("Entered value is greater than the allowed!")
            else:
                if out:
                    print(f"Current voltage: {self._output(int(value))}")
                else:
                    self._output(int(value))

    def _output(self, value: int):
        GPIO.output(self.pins, dec2bin(value))
        return "{:.4f}".format(value * 3.3 / 256)
    
    def close(self):
        GPIO.output(self.pins, 0)
        GPIO.cleanup()
