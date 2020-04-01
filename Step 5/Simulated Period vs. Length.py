#!/usr/bin/env python3

# Simulated Period vs. Length.py

# Odin Doolittle and Athena Ohnemus
# We worked alone on this script.
# This script uses simulated periods for different lengths and plots them.

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:19:43 2020

@author: odindoolittle
"""
import matplotlib.pyplot as plt

Period = [1.256, 1.412, 1.568, 1.696, 1.827]
Length = [.34, .43, .53, .62, .72]

plt.plot(Length, Period)
plt.xlabel('Length (m)')
plt.ylabel('Period (s)')
plt.suptitle('Length vs. Period Simulation Data')
plt.ylim(1.1, 1.9)
plt.show()