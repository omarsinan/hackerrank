# author: Omar Sinan
# date: 01/09/2017
# description: HackerRank's "Day 6: Let's Review" Coding Challenge

n = int(raw_input())
strings = []
for i in range(n):
    s = raw_input()
    strings.append(s)
    
for i in strings:
    print i[::2], i[1::2]
