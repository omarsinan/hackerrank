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
