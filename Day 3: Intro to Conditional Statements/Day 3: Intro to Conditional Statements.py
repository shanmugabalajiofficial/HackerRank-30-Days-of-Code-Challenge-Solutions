#Day 3: Intro to Conditional Statements


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
if N % 2 != 0:
    print("Weird")
elif N % 2 == 0 and 1<N<6:
    print("Not Weird")
elif N % 2== 0 and 5<N<21:
    print("Weird")
else:
    print("Not Weird")
