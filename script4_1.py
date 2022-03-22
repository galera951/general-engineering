from ledCls import Leds

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


leds = Leds()

try:
    while True:
        value = input('Please enter a number from [0, 255] interval: ')

        if value == "q":
            raise Exception("exit")
        
        leds.push(value, out=True)

except Exception as e:
    if str(e) == "exit":
        print("Exit successfully!")

finally:
    leds.close()