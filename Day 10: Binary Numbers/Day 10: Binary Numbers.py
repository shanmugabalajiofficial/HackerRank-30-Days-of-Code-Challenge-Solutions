#Day 10: Binary Numbers


#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
print(len(max("{0:b}".format(n).split('0'))))
