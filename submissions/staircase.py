
# author: Omar Sinan
# date: 25/08/2017
# description: HackerRank's "Staircase" Coding Challenge

#!/bin/python

import sys

n = int(raw_input().strip())
spaces = n - 1
hashes = 1

for i in range(n):
    for j in range(spaces):
        sys.stdout.write(' ')
    for k in range(hashes):
        sys.stdout.write('#')
    hashes += 1
    spaces -= 1
    print
