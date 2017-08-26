# author: Omar Sinan
# date: 26/08/2017
# description: HackerRank's "Merge the Tools!" Coding Challenge

def merge_the_tools(string, k):
    segs = []
    for i in range(0, len(string), k):
        segs.append(string[i : i + k])
        
    for seg in segs:
        occurances = []
        for i in seg:
            if i not in occurances:
                occurances.append(i)
        print ''.join(occurances)
    
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
