##################
# Receiver.py

# Athena Ohnemus and Odin Doolittle
# TAs Assisted us with this script.
# This script receives acceleration data as a script with radio signals.
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=16, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio
    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        mb.sleep(10)
        l = incoming.split(',')
        data = (int(l[0]),int(l[1]),int(l[2]),int(l[3]))
        print(data)