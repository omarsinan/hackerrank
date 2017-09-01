# author: Omar Sinan
# date: 01/09/2017
# description: HackerRank's "Bot saves princess" Coding Challenge

#!/bin/python

def displayPathtoPrincess(n,grid):
    commands = []
    for index,val in enumerate(grid):
        if "m" in val:
            m = [index, val.index('m')]
        if "p" in val:
            p = [index, val.index('p')]
    while m[0] != p[0] and m[1] != p[1]:
        if p[0] > m[0]:
            commands.append('DOWN')
            m[0] += 1
        elif p[0] < m[0]:
            commands.append('UP')
            m[0] -= 1
        if p[1] > m[1]:
            commands.append('RIGHT')
            m[1] += 1
        elif p[1] < m[1]:
            commands.append('LEFT')
            m[1] -= 1
            
    for i in commands: print i
    
m = input()
grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
