import math
def func():
    c,n = map(int,input().split(' '))
    t = int((n * (n + 1)) / 2)
    k = int(c/n)
    m = int((n*(n-1))/2)
    if t > c:
        print(c)
    else:
        for i in range(k,0,-1):
            # l = int((i*(i+1)/2))
            l = int((i * n)) + (m)
            if ( l <= c):
                print(int(c-l))
                break
    
T = int(input())
while(T>0):
    func()
    T = T-1
