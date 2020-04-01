 ##################
# logger.py

# Odin Doolittle and Athena Ohnemus.
# We had help from TAs for this script.
# This script sends acceleration info by radio to another microbit.
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=16, length=100)

print('Program Started')

mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging
string = ""


while not mb.button_a.is_pressed():
    x = mb.accelerometer.get_x()
    y = mb.accelerometer.get_y()
    z = mb.accelerometer.get_z()
    radio.send(str(mb.running_time()) + ',' + str(x) + ',' + str(y) + ',' + str(z))

    mb.sleep(10)

mb.display.show(mb.Image.SQUARE)  # Display Square when program ends