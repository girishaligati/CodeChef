from collections import deque
#No need of deque
T = int(input())
while (T>0):
    count,maxi = 0,0
    E = input()
    li = deque()
    for i in E:
        if i == '>':
            if (len(li) != 0):
                li.pop()
                count = count + 2
            else:
                break
        else:
            li.append(i)
        if (count > maxi and len(li) == 0):
            maxi = count
    print(maxi)
    T = T - 1