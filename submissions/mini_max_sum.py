
# author: Omar Sinan
# date: 26/08/2017
# description: HackerRank's "Mini-Max Sum" Coding Challenge

#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
tempArr = list(arr)
results = []
for i in arr:
    tempArr.remove(i)
    sum = 0
    for i in tempArr:
        sum += i
    results.append(sum)
    tempArr = list(arr)

print min(results), max(results)
