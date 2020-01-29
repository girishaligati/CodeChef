Q = int(input())
S = input()
while (Q>0):
    arr = [0]*26
    flag = 0
    L,R = map(int,input().split(' '))
    for i in S[L-1:R]:
        arr[ord(i) - ord('a')] = arr[ord(i) - ord('a')] + 1
    for i in arr:
        if i % 2 != 0 :
            flag = flag + 1
    if flag > 1:
            print("Impossible")
    else:
        print("Possible")
    Q = Q - 1