# author: Omar Sinan
# date: 26/08/2017
# description: HackerRank's "Grading Students" Coding Challenge

#!/bin/python

import sys
import math

def solve(grades):
    for i, val in enumerate(grades):
        next_multiple = 5 * math.ceil(val / 5.0)
        if next_multiple - val < 3 and val >= 38:
            grades[i] = int(next_multiple)
    return grades

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))


