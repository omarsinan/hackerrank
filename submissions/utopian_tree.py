# author: Omar Sinan
# date: 04/09/2017
# description: HackerRank's "Utopian Tree" Coding Challenge

#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    result = 1
    for i in range(n):
        if i % 2 == 0:
            result *= 2
        else:
            result += 1
    print result
