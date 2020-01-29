import math
def func():
    N = int(input())
    A = list(map(int,input().split(' ')))
    count = 1
    flag = 0
    if N % 2 == 0:
        h = int(N/2)
        # print("In 1st half")
        for i in range(h):
            if ((A[i] - count) == 0 and A[i] <= 10):
                pass
            elif((A[i] - count) == 1 and A[i] <= 10):
                count = count + 1
            else:
                flag = 1
                break
        if (flag == 0):
            A2 = A[h:]
            # print(A[:h],A2)
            A2.reverse()
            # print(A[:h],A2)
            if A[:h] == A2:
                print("yes")
            else:
                print("no")
        else:
            print("no")

    else:
        h = int(N/2)
        for i in range(h+1):
            if ((A[i] - count) == 0 and A[i] <= 10):
                pass
            elif((A[i] - count) == 1 and A[i] <= 10):
                count = count + 1
            else:
                flag = 1
                break
        if (flag == 0):
            A2 = A[h+1:]
            A2.reverse()
            # print(A,A2,A[:h])
            if A[:h] == A2:
                print("yes")
            else:
                print("no")
        else:
            print("no")
    

T = int(input())
while(T>0):
    func()
    T = T-1
