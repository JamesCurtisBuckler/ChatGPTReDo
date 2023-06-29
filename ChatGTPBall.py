# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 17:29:17 2023

@author: James Curtis Buckler
"""

def calculate_max_height(v0, g):
    max_height = (v0 ** 2) / (2 * g)
    return max_height

# Taking inputs from the console
v0 = float(input("Enter the initial velocity of the ball (ft/sec): "))
g = 32.8  # Acceleration due to gravity (ft/sec^2)

# Calculate the maximum height
max_height = calculate_max_height(v0, g)

# Print the result
print(f"The maximum height reached by the ball is: {max_height} ft")
