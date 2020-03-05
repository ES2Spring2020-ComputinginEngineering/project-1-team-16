##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately
fout = open('data_file', 'w')
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

        #############################################################
        # FILL IN HERE
        # Incoming is string sent from logger
        # Need to parse it and reformat as a tuple for the MU plotter
        #############################################################
        mb.sleep(10)
        l = incoming.split(',')
        data = (int(l[0]),int(l[1]),int(l[2]),int(l[3]))
        print(data)

fout.write(data)

fout.close()