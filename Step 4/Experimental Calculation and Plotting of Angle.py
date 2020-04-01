#!/usr/bin/env python3

# Experimental Calculation and Plotting of Angle.py

# Athena Ohnemus and Odin Doolittle
# TAs and Proffesor Cross helped us with this script.
# This script finds angle using acceleration and plots it with time. 

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:08:36 2020

@author: odindoolittle
"""


import matplotlib.pyplot as plt
import math
import os

path = '/Users/odindoolittle/Documents/GitHub/project-1-team-16/Step 3'
os.chdir(path)
cwd = os.getcwd()
print(cwd)

fin = open('dataset3_53cm.csv', 'r')
time = []
ax = []
x_array = []
ay = []
y_array = []
az = []
z_array = []
theta = []


def tilt_X(x_val, y_val, z_val):
    # This function takes the x, y, and z value of raw acceleration as parameters.
    # It uses these accel values to find the angle.
    # It returns this angle as ang_x in degrees
    x= (x_val/(math.sqrt(y_val**2+z_val**2)))
    ang_x = math.atan(x)*180/math.pi
    return ang_x

for i in fin:
    lines = i.split(',')
    if 20000 < int(lines[0]) < 30000:
        time.append((int(lines[0])/1000))
        ax = float(lines[1])
        x_array.append(ax)
        ay = float(lines[2])
        y_array.append(ay)
        az = float(lines[3])
        z_array.append(az)
        if ax == 0 and az == 0:
            pass
        theta.append(tilt_X(ay,ax,az))

plt.suptitle('Data Set 3:53 cm', y = 1, fontsize = 18)
plt.title('Angle vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.axis()
plt.plot(time, theta, color = 'teal')
plt.show()