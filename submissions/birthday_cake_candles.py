# author: Omar Sinan
# date: 26/08/2017
# description: HackerRank's "Birthday Cake Candles" Coding Challenge

#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    maxH = max(ar)
    return ar.count(maxH)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
