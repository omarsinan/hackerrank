# author: Omar Sinan
# date: 03/09/2017
# description: HackerRank's "Fibonacci Modified" Coding Challenge

inp = map(int, raw_input().split())
numbers = [inp[0], inp[1]]
for i in range(inp[2]):
    numbers.append((numbers[i]) + (numbers[i + 1])**2)
print numbers[inp[2] - 1]
