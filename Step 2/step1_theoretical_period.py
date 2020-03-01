# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:33:54 2020

@author: athen
"""
# The real world pendulum will never behave exactly as the model does. 
# In the real world, the pendulum will have a frictional and air resistance force in the opposite direction of its motion.  decreasing the period.
# The resisting force will decrease the acceleration and velocity of the pendulum, increasing its period.
# Another factor to consider is that a perfect pendulum has a string with negligible mass and all of its weight centered at the end. 
# Our pendulum has mass throughout so its center of mass is not at the end and therefor the "length" is not the length of the pendulum.
# For the theoretical model we assume the length is the length of the entire pendulum and there is no resisting force. 

import numpy as np
import math
import matplotlib.pyplot as plt

length_array_meters= (.0254*np.array([26.75, 24.75, 22.75, 20.25, 18.25]))

def period(length_inches):
    return (2*math.pi*np.sqrt(length_inches*(1/9.805)))

print(period(length_array_meters))

plt.plot(period(length_array_meters), length_array_meters )
plt.ylabel('length (m)')
plt.xlabel('period (s)')
plt.show()
