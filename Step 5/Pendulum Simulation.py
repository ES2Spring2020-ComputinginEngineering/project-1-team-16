#!/usr/bin/env python3

# Pendulum Simulation.py
# Athena Ohnemus and Odin Doolittle
# We received help from Andrew Sack on this script.
# This script creates a simulation of a theoretical pendulum and graphs it.

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:46:23 2020

@author: odindoolittle
"""
import math
import numpy as np
import os
import matplotlib.pyplot as plt
import scipy.signal as sig

path = '/Users/odindoolittle/Documents/GitHub/project-1-team-16/Step 3'
os.chdir(path)
cwd = os.getcwd()
print(cwd)
print('Hello World!')

fin = open('dataset1_34cm.csv')
t = []
elapsed_t_list = []
time = []
pos = [math.pi/3]
vel = [0.0]
acc = [0.0]
time = np.linspace(0,10,100000)
i = 1

def update_system(acc,pos,vel,time1,time2):
    # This function takes acceleration, angle (position), velocity, a time, 
    # and the previous time as arguments.
    # It predicts the next angle, velocity, and acceleration.
    # It returns angle, velocity, and position (angle).
    dt = time2-time1
    accNext = -(math.sin(pos)*9.805/(.34))
    velNext = vel+accNext*dt
    posNext = pos+velNext*dt
    return accNext, velNext,posNext

def print_system(time,pos,vel):
    # This funciton takes time, position, and velocity as arguments.
    # It prints the value of each with a label.
    # It has no return value.
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

def period():
    # This function takes no arguments.
    # It builds up a tally for the number of peaks and tracks the time between 
    #each peak.
    # It returns a list of the period lengths.
    n = 0
    for i in theta_pks: 
        n += 1
        t.append(time[i])
        if n >= 2:
            elapsed_t = t[n-1]-t[n-2]           
            elapsed_t_list.append(elapsed_t)            
    return elapsed_t_list
    
def avg_period(elapsed_t_list):
    # This function takes the list of periods as an arugment.
    # It sums them and divides by the number of inputs to find an average.
    # It returns the average period.
    n = 0
    elapsed_t_total = 0
    elapsed_t_total = sum(elapsed_t_list)
    for i in elapsed_t_list:
        n += 1
    return (elapsed_t_total/n)

while i < len(time):
    n = i
    accNext, velNext, posNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    acc.append(accNext)
    i += 1
    
print_system(time[0],pos[0],vel[0])

plt.suptitle('Pendulum Simulation: 34cm & pi/3', y = 1.6, fontsize = 18)
plt.subplot(311)
plt.plot(time, acc, color = 'green')
plt.ylabel('Acceleration (rad/sec^2)')
plt.subplot(312)
plt.plot(time, vel, color = 'blue')
plt.ylabel('Velocity (rad/sec)')
plt.subplot(313)
plt.plot(time, pos, color = 'red')
plt.xlabel('Time (sec)')
plt.ylabel('Position (rad)')
plt.subplots_adjust(bottom=0.1, right=0.8, top=1.5, hspace = 0.2)

plt.show()

theta_filt = sig.medfilt(pos, 1)
theta_pks, _ = sig.find_peaks(theta_filt)

plt.plot(time, theta_filt, 'r-', time[theta_pks], theta_filt[theta_pks], 'b.')
plt.ylabel('Angle (rad)')
plt.xlabel('Time (sec)')
plt.suptitle('34cm: Angle vs Time with Peaks', fontsize = 18)

print(avg_period(period()))