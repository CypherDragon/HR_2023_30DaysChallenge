#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip_dec = tip_percent/100 # Convert tip integer to decimal value
    tip_total = meal_cost * tip_dec # Calculate amount of tip
    
    tax_dec = tax_percent/100 # Convert tax integer to decimal value
    tax_total = meal_cost * tax_dec # Calculate amount of tax
    
    total = meal_cost + tip_total + tax_total # Calculate total meal cost
    print(round(total)) # Round to nearest integer, as required by problem

if __name__ == '__main__': # Provided by problem
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
