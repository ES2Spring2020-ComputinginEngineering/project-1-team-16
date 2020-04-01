#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:05:54 2020

@author: odindoolittle
"""
import matplotlib.pyplot as plt

lengths = [.34, .43, .53, .62, .72]

Theory = [1.170, 1.316, 1.461, 1.580, 1.703]
Exp = [1.178, 1.314, 1.425, 1.535, 1.637]
Sim = [1.256, 1.412, 1.568, 1.696, 1.827]

plt.plot(lengths, Theory, color = 'blue', label = 'Theoretical Data')
plt.legend()
plt.plot(lengths, Exp, color = 'green', label = 'Experimental Data')
plt.legend()
plt.plot(lengths, Sim, color = 'orange', label = 'Simulation Data')
plt.legend()
plt.yscale('log')
plt.grid(True)
plt.title('Log Comparison Length vs. Period')
plt.ylabel('Period (seconds)')
plt.xlabel('Length (meters)')