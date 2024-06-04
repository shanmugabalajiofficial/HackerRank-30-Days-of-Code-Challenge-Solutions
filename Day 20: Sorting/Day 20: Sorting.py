#Day 20: Sorting


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
n = len(a)
numberOfSwaps = 0

for i in range(n):
    for j in range(n - i - 1):
        # Swap adjacent elements if they are in decreasing order
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1
    
    # If no elements were swapped during a traversal, the array is sorted
    if numberOfSwaps == 0:
        break
print(f"Array is sorted in {numberOfSwaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
