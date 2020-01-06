# Lost Guy Radhu Problem Code: MAY19F1
# https://www.codechef.com/FLPAST01/problems/MAY19F1

T = int(input())
while (T>0):
    N,Q = map(int,input().split(' '))
    A = list(map(int,input().split(' ')))
    q = list(map(int,input().split(' ')))
    b=[]
    b.append(A[0])
    for i in range(len(A)-1):
        if A[i+1] > b[i]:
             b.append(A[i+1])
        else:
             b.append(b[i])
    for i in q:
        print(b[i-1])
    T = T - 1

"""
Sample Input:

1        
5 3        
5 4 8 6 9        
2 3 5

Sample Output:

5        
8        
9    

"""