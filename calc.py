import RPi.GPIO as GPIO
import time

#configs
pins = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
action_pin = 3
plus_pin = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.setup([action_pin, plus_pin], GPIO.IN)

#functions
def bin_output(number: int):
    to_bin = list(map(int, str(bin(number))[2:]))
    #print(to_bin)
    out = ([False for i in range(8)] + list(map(bool, to_bin)))[-8:]
    #print(out)
    GPIO.output(pins,  out)

def start_program():
    for pin in pins:
        GPIO.output(pin, 1)
        time.sleep(1/8)
    GPIO.output(pins, 0)

def end_program():
    for i in range(len(pins) + 1, 0, -1):
        GPIO.output(pins[:i], 1)
        GPIO.output(pins[i - 1:], 0)
        time.sleep(1/8)
    GPIO.output(pins, 0)

def action_output():
    for i in range(3, -1, -1):
        GPIO.output(pins, 0)
        GPIO.output([pins[i], pins[7 - i]], 1)
        time.sleep(1/8)
    GPIO.output(pins, 0)

def plus():
    if GPIO.input(plus_pin):
        while GPIO.input(plus_pin):
            continue
        time.sleep(0.8)
        return True
    else:
        return False

def action():
    if GPIO.input(action_pin):
        while GPIO.input(action_pin):
            continue
        time.sleep(0.8)
        return True
    else:
        return False

def matem(number1, number2, act):
    print(act)
    if act == 0:
        return number1 + number2

    elif act == 1:
        return number1 * number2
    
    elif act == 2:
        return number1 % number2

    elif act == 3:
        return number1 ** number2

def main():
    act = 0
    number1 = 0
    number2 = 0

    while True:
        if plus():
            number1 += 1
            bin_output(number1)
        elif action():
            print(number1)
            action_output()
            break

    while True:
        if plus():
            number2 += 1
            bin_output(number2)

        elif action():
            if number2 == 0:
                act += 1
                action_output()
            else:
                print(number2)
                print('=')

                action_output()
                result = matem(number1, number2, act)

                print(result)
                bin_output(result)

                time.sleep(10)
                
                break

#start program
if __name__ == '__main__':
    start_program()
    main()
    end_program()
