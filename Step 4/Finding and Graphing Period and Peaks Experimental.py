#!/usr/bin/env python3

# Finding and Graphing Period and Peaks Experimental.py
# Athena Ohnemus and Odin Doolittle
# We received help from TAs on this script.
# This script finds peaks on an angle vs. time graph and finds an average period.
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:00:08 2020

@author: odindoolittle
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import math
import scipy.signal as sig

path = '/Users/odindoolittle/Documents/GitHub/project-1-team-16/Step 3'
os.chdir(path)
cwd = os.getcwd()
print(cwd)

fin1 = open('dataset5_72cm.csv', 'r')
time = []
ax = []
ay = []
zwithn = []
az = []
theta = []
t = []
elapsed_t_list = []

def tiltx(x, y, z):
    # This function takes the x, y, and z value of raw acceleration as parameters.
    # It uses these accel values to find the angle.
    # It returns this angle
    a = x
    b = (math.sqrt(y**2+z**2))
    return float((math.atan2(a, b))*(180/math.pi))

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

for i in fin1:
    lines = i.split(',')
    if 20000 < int(lines[0]) < 30000:
        time.append((int(lines[0])/1000))
        ax = (float(lines[1])/1000)*9.8
        ay = (float(lines[2])/1000)*9.8
        az = (float(lines[3])/1000)*9.8
        if ax == 0 and az == 0:
            pass
        theta.append(tiltx(ay,ax,az))

theta_filt = sig.medfilt(theta, 17)
theta_pks, _ = sig.find_peaks(theta_filt, height = 1.25, distance = 30)
time = np.asarray(time)
plt.plot(time, theta_filt, 'r-', time[theta_pks], theta_filt[theta_pks], 'b.')
plt.ylabel('Angle (rad)')
plt.xlabel('Time (sec)')
plt.suptitle('72cm: Angle vs Time with Peaks', fontsize = 18)
print(avg_period(period()))