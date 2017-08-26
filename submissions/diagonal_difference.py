# author: Omar Sinan
# date: 26/08/2017
# description: HackerRank's "Diagonal Difference" Coding Challenge

#!/bin/python

import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

sum = 0
for i in range(n):
    sum += a[i][i] - a[i][len(a[i]) - 1 - i]
    
print abs(sum)
