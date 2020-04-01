# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:33:54 2020

@author: athen
"""
# Theoretical Calculation and Plot Period

# Athena Ohnemus and Odin Doolittle
# This project was completed with the help of TAs and Professor Cross.
# This script is step two for Project 1. It calculates and plots theoretical
#period for different pendulum lengths.




# The real world pendulum will never behave exactly as the model does. 
# In the real world, the pendulum will have a frictional and air resistance 
#force in the opposite direction of its motion.  decreasing the period.
# The resisting force will decrease the acceleration and velocity of the 
#pendulum, increasing its period.
# Another factor to consider is that a perfect pendulum has a string with 
#negligible mass and all of its weight centered at the end. 
# Our pendulum has mass throughout so its center of mass is not at the end and 
#therefor the "length" is not the length of the pendulum.
# For the theoretical model we assume the length is the length of the entire 
#pendulum and there is no resisting force. 

import numpy as np
import math
import matplotlib.pyplot as plt

length_array_meters = np.array([.34, .43, .53, .62, .72])

def period(length):
    #This function takes length (m) as a parameter. 
    #It uses a physics formula to calculate a theoretical period.
    #It returns this theoretical period.
    #This function has serious limitations. In using the length of the pendulum it is assuming
    #that the pendulum is connected to its pivot point by a weightless string with all of its mass concentrated
    #at the end length. It also ignores outside forces such as friction and air resistance.
    return (2*math.pi*np.sqrt(length*(1/9.805)))

print(period(length_array_meters))
plt.plot(length_array_meters, period(length_array_meters))
plt.xlabel('Length (m)')
plt.ylabel('Period (s)')
plt.ylim(1.1, 1.9)
plt.suptitle('Theoretical Length vs. Period')
plt.show()
