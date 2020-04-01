#!/usr/bin/env python3
# Experimental Length vs Period.py

# Odin Doolittle and Athena Ohnemus
# We received no help for this script.
# This script graphs obtained average period values with their length.
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:26:56 2020
@author: odindoolittle
"""
import matplotlib.pyplot as plt

lengths = [.34, .43, .53, .62, .72]
periods = [1.178, 1.314, 1.425, 1.535, 1.637]

plt.plot(lengths, periods)
plt.xlabel('Length (m)')
plt.ylabel('Period (s)')
plt.ylim(1.1, 1.9)
plt.suptitle('Length vs. Period Experimental Data')