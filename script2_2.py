import RPi.GPIO as GPIO

#configs
pins = [10, 9, 11, 5, 6, 13, 19, 26][::-1]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)


def bin_output(number: int):
    to_bin = list(map(int, str(bin(number))[2:]))
    #print(to_bin)
    out = ([False for i in range(8)] + list(map(bool, to_bin)))[-8:]
    #print(out)
    GPIO.output(pins,  out)

def main_1():

    while True:
        inp = input('Type your number or "exit" to exit: ')

        if inp == 'exit':
            GPIO.output(pins, 0)
            GPIO.cleanup()
            break

        try:
            number = int(inp)
        except:
            print('Please type a number.')
            continue

        if number > 255:
            print('Too much!')
            continue
        
        bin_output(number)


if __name__ == '__main__':
    main_1()