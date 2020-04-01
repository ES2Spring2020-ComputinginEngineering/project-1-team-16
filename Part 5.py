#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:46:23 2020

@author: odindoolittle
"""
import math
import numpy as np
import os
import matplotlib.pyplot as plt
path = '/Users/odindoolittle/Documents/GitHub/project-1-team-16/Step 3'
os.chdir(path)
cwd = os.getcwd()
print(cwd)
print('Hello World!')

fin = open('dataset1_34cm.csv')


def update_system(acc,pos,vel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    accNext = -(math.sin(pos)*9.805/(.22))
    velNext = vel+accNext*dt
    posNext = pos+velNext*dt
    return accNext, velNext,posNext

def print_system(time,pos,vel):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

# initial conditions


time = []
pos = [math.pi/3]
vel = [0.0]
acc = [0.0]
time = np.linspace(0,10,100000)
print_system(time[0],pos[0],vel[0])


i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    n = i
    accNext, velNext, posNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    acc.append(accNext)
#    print_system(time[i],pos[i],vel[i])
    i += 1

plt.suptitle('Pendulum Simulation', y = 1.6, fontsize = 18)
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