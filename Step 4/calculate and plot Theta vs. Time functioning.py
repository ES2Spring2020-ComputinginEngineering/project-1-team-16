#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:55:20 2020

@author: odindoolittle
"""

import matplotlib as plt
import math
import os

path = '/Users/odindoolittle/Documents/GitHub/project-1-team-16/Step 4'
os.chdir(path)
cwd = os.getcwd()
print(cwd)

fin1 = open('dataset5_72cm.csv', 'r')

def tilt_X(x_val, y_val, z_val):
    x= (x_val/(math.sqrt(y_val**2+z_val**2)))
    ang_x = math.atan(x)
    return ang_x


def tilt_Y(x_val, y_val, z_val):
    y=(y_val/(math.sqrt(x_val**2+z_val**2)))
    ang_y=math.atan(y)
    return ang_y

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
        
print(tilt_Y(ax,ay,az))
print(tilt_X(ax, ay, az))