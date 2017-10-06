# author: Omar Sinan
# date: 26/08/2017
# updated: 06/10/2017 - After 2 months of python, I decided to revist this challenge
# description: HackerRank's "The Minnion Game" Coding Challenge

def minion_game(string):
        k = s = 0 #kevin: vowels
        
        k = sum([len(string) - i for i in range(len(string)) if string[i] in 'AEIOU'])
        s = sum([len(string) - i for i in range(len(string)) if string[i] not in 'AEIOU'])
        
        if s > k:
            print "Stuart", s
        elif k > s:
            print "Kevin", k
        else:
            print "Draw"
       
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
