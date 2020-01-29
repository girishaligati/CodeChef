T = int(input())
while (T>0):
    E = input().strip()
    d = {'C':12,'O':16,'H':1}
    li = []
    for i in E:
        if(i == "("):
            print("In ( if")
            li.append(i)
        elif(i=="C" or i=="O" or i=="H" or (i>="2" and i<="9")):
            print("in C if")
            if(len(li) == 0):
                li.append(d[i])
            elif (li[-1] != '('):
                if i.isalpha():
                    li.append(int(d[i]))
                else:
                    li.append(int(li.pop()*int(i)))
            else:
                li.append(d[i])
            print(li)
        elif (i == ")"):
            count = 0
            print("In ) if")
            print(li)
            while(li[-1] != '('):
                count = count + li.pop()
            li.pop()
            li.append(count)
    print(sum(li))
    T = T - 1