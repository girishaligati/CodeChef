# Math and Games Problem Code: RADGEE
# https://www.codechef.com/FLPAST01/problems/RADGEE

from collections import deque
T = int(input())
while (T>0):
    N,M = map(int,input().split(' '))
    R = deque(map(int,input().split(' ')))
    G = deque(map(int,input().split(' ')))
    C = deque(map(int,input().split(' ')))
    # R.reverse()
    # G.reverse()
    # C.reverse()
    R_wins = 0
    G_wins = 0
    while(len(R) > 0 and len(G) > 0):
        if(R.popleft() > G.popleft()):
            R_wins = R_wins+1
            if(len(C) > 0):
                R.append(C.popleft())
                G.append(C.popleft())
        else:
            G_wins = G_wins+1
            if(len(C) > 0):
                G.append(C.popleft())
                R.append(C.popleft())
    if(R_wins > G_wins):
        print("Radhesh wins")
    elif(R_wins == G_wins):
        print("Tie")
    else:
        print("Geethakoomaree wins")
    T = T - 1



"""
    Sample Input:

3
5 4
1 4 7 10 12
3 6 4 8 22
7 8 9 14
1 2
1
5
2 5
5 2
1 2 3 4 5
10 9 8 7 6
12 11

Sample Output:

Radhesh wins
Tie
Geethakoomaree wins
"""