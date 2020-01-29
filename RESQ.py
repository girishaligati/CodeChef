import math
def func():
    N = int(input())
    # j = float('inf')
    i = int(math.sqrt(N))
    for k in range(i,0,-1):
        if N % k == 0:
            j = N / k
            return(int(j-k))


T = int(input())
while(T>0):
    print(func())
    T = T-1
