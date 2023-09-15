#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# Input (stdin)
# 8
# UDDDUDUU

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    altitude = 0
    
    for step in path:
        if step == "D":
            if altitude == 0:
                valleys += 1
            altitude -= 1
        elif step =="U":
            altitude += 1
    return valleys
