# Question from SPOJ
from collections import deque
T = int(input())
while (T>0):
    N = int(input())
    A = list(map(int,input().split(' ')))
    S = deque(A)
    Q = []
    flag = 0
    while (len(S) >= 2):
        if (S[-1] > S[-2]):
            Q.append(S.pop())
            Q.sort()
            for i in range(len(Q)):
                if (S[-1] < Q[i]):
                    S[-1],Q[i] = Q[i],S[-1]
                    S.extend(Q)
                    flag = 1
                    print("".join(map(str,A)))
                    print("".join(map(str,S)))
                    break
            break
        else:
            Q.append(S.pop())
    if flag == 1:
        pass
    else:
        print('NO NXTBIG')
    T = T - 1