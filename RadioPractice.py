import radio
import random
from microbit import *
radio.on()

while True:
    sleep(20)
    radio.send(str(accelerometer.get_values()))
