def minion_game(string):
    k = s = 0 #kevin: vowels
    for i, val in enumerate(string):
        if val in 'AEIOU':
            k += len(string) - i
        else:
            s += len(string) - i

    if s > k:
        print "Stuart", s
    elif k > s:
        print "Kevin", k
    else:
        print "Draw"
       
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
