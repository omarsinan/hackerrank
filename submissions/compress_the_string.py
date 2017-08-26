# author: Omar Sinan
# date: 26/08/2017
# description: HackerRank's "Compress the String!" Coding Challenge

from itertools import groupby

def compress(s):
    l = list(s)
    for key, group in groupby(l):
        print "(" + str(len(list(group))) + ", " + str(key[0])+ ")",
        
if __name__ == "__main__":
    s = raw_input()
    compress(s)
