# Is this FFT #
##### https://www.codechef.com/FLPAST01/problems/POLMUL #####

T = int(input())
while (T>0):
    N,M = map(int,input().split(' '))
    P = list(map(int,input().split(' ')))
    Q = list(map(int,input().split(' ')))
    b=[0 for i in range(M+N-1)]
    for i in range(len(P)):
        for j in range(len(Q)):
            b[i+j] = b[i+j]+(P[i]*Q[j])
    print(*b)
    T = T - 1

"""
Sample Input:

3

2 2
1 -1
1 1

3 2
1 2 1
0 1

3 3
1 2 1
1 -2 1

Sample Output:

1 0 -1 
0 1 2 1 
1 0 -2 0 1 
"""