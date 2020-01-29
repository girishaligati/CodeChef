T = int(input())
while(T > 0):
    flag = 0
    S = input()
    i = 0
    count = 0
    l = len(S)
    while(i < l):
        if (S[i] == '1' and count == 0):
            while(S[i] != '0' and i < l-1):
                # print(i)
                count = count+1
                i = i+1
            i = i+count-1
            flag = 1
        elif(S[i]== '1' and count != 0):
            flag = 0
            # print("NO")
            break
        else:
            i = i+1 
    if (flag == 1):
        print("YES")
    else:
        print("NO")
    T = T - 1