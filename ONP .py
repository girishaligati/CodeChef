T = int(input())
while (T>0):
    e = []
    rpn = []
    S = input()
    for i in S:
        if (i == '(' or i == '+' or i == '-' or i == '*' or i == '^'):
            e.append(i)
        elif (i >= 'a' and i <= 'z'):
            rpn.append(i)
        elif (i == ')'):
            while(len(e) != 0 and e[-1] != '('):
                rpn.append(e.pop())
            if(e[-1] == '('):
                e.pop()
    while(len(e)!=0):
        rpn.append(e.pop())
    print(''.join(rpn))
    T = T - 1