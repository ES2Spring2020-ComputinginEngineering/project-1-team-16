# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:33:54 2020

@author: athen
"""

import numpy as np
import math
import matplotlib.pyplot as plt

length_array_meters= (.0254*np.array([26.75, 24.75, 22.75, 20.25, 18.25]))

def period(length_inches):
    return (2*math.pi*np.sqrt(length_inches*(1/9.805)))

print(period(length_array_meters))

#length_vs_period = 

plt.plot(period(length_array_meters), length_array_meters )
plt.ylabel('length (m)')
plt.xlabel('period (s)')
plt.show()
