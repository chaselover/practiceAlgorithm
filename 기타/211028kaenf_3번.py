#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minOperations' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def minOperations(n):
    bin_n = list(map(int, bin(n)[2:].lstrip('0')))
    return bin_n

if __name__ == '__main__':

    n = int(input().strip())

    result = minOperations(n)

    print(result)

