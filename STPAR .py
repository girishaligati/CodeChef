from collections import deque

while(1):
    T = int(input())
    if T == 0:
        break
    flag = 0
    li = []
    target = 1
    E = deque(map(int,input().split()))
    for i in range(T):
        while(len(li) != 0 and li[-1] == target):
            li.pop()
            target = target + 1
        if(E[0] == target):
            E.popleft()
            target = target + 1
        elif(len(li) != 0 and li[-1] < E[0]):
            flag = 1
            break
        else:
            li.append(E.popleft())
    if flag == 0:
        print('yes')
    else:
        print('no')