T = int(input())
while (T>0):
    N,K = map(int,input().split(' '))
    P = list(map(int,input().split(' ')))
    char_values = [x+K for x in P]
    count = 0
    for x in char_values:
        if not x%7:
            count = count+1
    print(count)
    T = T - 1