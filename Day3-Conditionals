#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    if N < 1 and N > 100: # Verify input is not out of desired range (1-100)
        print("Number out of range")
    
    else:
        if N%2 != 0: # Compare input to remainder if divided by 2. Simple check if value is odd or even
            print("Weird")
            
        else: 
            if N >= 2 and N < 5: # First group after the odd/even check
                print("Not Weird")
                
            if N >= 6 and N <= 20: # Second group after the odd/even check
                print("Weird")
            
            if N > 20: # Final group
                print("Not Weird")
