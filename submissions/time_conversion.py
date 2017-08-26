# author: Omar Sinan
# date: 26/08/2017
# description: HackerRank's "Time Conversion" Coding Challenge

#!/bin/python

import sys

def timeConversion(s):
    t = 0
    arr = s.split(':')
    if "PM" in arr[len(arr) - 1]:
        t = 1
        arr[len(arr) - 1] = arr[len(arr) - 1].replace('PM', '')
    else:
        arr[len(arr) - 1] = arr[len(arr) - 1].replace('AM', '')
        
    if t:
        if not int(arr[0]) == 12:
            arr[0] = str(int(arr[0]) + 12)
    else:
        if int(arr[0]) == 12:
            arr[0] = "00"
    
    return ":".join(str(item) for item in arr)

s = raw_input().strip()
result = timeConversion(s)
print(result)
