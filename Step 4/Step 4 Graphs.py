#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:18:40 2020

@author: odindoolittle
"""
import numpy as np
import matplotlib.pyplot as plt
import os
path = '/Users/odindoolittle/Documents/GitHub/project-1-team-16/Step 4'
os.chdir(path)
cwd = os.getcwd()
print(cwd)

fin1 = open('dataset5_72cm.csv', 'r')



time = []
ax = []
ay = []
zwithn = []
az = []
for i in fin1:
    lines = i.split(',')
    if 10000 < int(lines[0]) < 15000:
        time.append((int(lines[0])/1000))
        ax.append(int(lines[1]))
        ay.append(int(lines[2]))
        az.append(int(lines[3]))


plt.suptitle("Data Set 5: 72 cm", y = 2.15, fontsize=18,)
plt.subplot(311)
plt.title('Ax vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m-g)')
plt.axis()
plt.plot(time, ax, color = 'teal')
plt.subplot(312)
plt.title('Ay vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m-g)')
plt.plot(time, ay, color = 'indigo')
plt.subplot(313)
plt.title('Az vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m-g)')
plt.plot(time, az, color = 'magenta')
plt.subplots_adjust(bottom=0.1, right=0.8, top=2, hspace = 0.5)


plt.show

