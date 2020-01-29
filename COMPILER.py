T = int(input())
while (T>0):
    E = input()
    count,maxi = 0,0
    li = []
    for i in E:
        if i == '<':
            li.append(i)
        elif(i == '>' and len(li) == 0):
            break
        else:
            if (len(li) == 0):
                pass
            elif (li.pop() == '<'):
                count = count + 2
                if(count >= maxi):
                    maxi = count
                # maxi = count
            else:
                pass
    if len(li) == 0:
        print(maxi)
    else:
        print('0')      
    T = T - 1