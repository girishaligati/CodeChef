T = int(input())
while (T>0):
    count = 0
    N = int(input())
    S = input()
    for i in range(len(S)):
        if S[i] == '1':
            for j in S[i:]:
                if  j == '1':
                    count = count + 1
    print(count)
    T = T - 1


T = int(input())
while (T>0):
    count = 0
    no_of_ones = 0
    N = int(input())
    S = input()
    for i in range(len(S)):
        if S[i] == '1':
            no_of_ones = no_of_ones + 1
            
            for j in S[i:]:
                if  j == '1':
                    count = count + 1
    print(count)
    T = T - 1