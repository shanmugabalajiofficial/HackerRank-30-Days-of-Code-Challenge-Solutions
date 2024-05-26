#Day 11: 2D Arrays


#!/bin/python3

import math
import os
import random
import re
import sys

def max_sum(arr):
    # keeping in mind the constraint of `-9 <= arr[i][j] <= 9`
    # minimum possible value we can have is -63 (if all value in the hourglass turns out to be -9)
    highest = -63
    for i in range(len(arr)-2):
        for j in range(len(arr[1])-2):
            top_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom_sum = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            hourglass_sum = top_sum + middle + bottom_sum
            
            if hourglass_sum > highest:
                highest = hourglass_sum
    print(highest)

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    max_sum(arr)
