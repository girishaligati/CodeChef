T = int(input())
while (T>0):
    word = input()
    li = []
    total=0
    for i in word:
        if (i == '{' and len(li) == 0):
            li.append(i)
            # print("1st If")
            # print(li,total)
        elif (i == '}' and len(li) == 0):
            li.append(i)
            # print("2st If")
            # print(li,total)
        elif (i == '}'and len(li) != 0):
            if(li[-1] == '{'):
                li.append(i)
                # print("3st If")
                # print(li,total)
            elif(li[-1] == '}'):
                if(len(li) <= 1 ):
                    li.pop()
                    total = total + 1
                    # print(li,total)
                    # print("4th If")
                else:
                    li.pop()
                    li.pop()
                    # print("5st If")
                    # print(li,total)
        elif (i == '{' and len(li) != 0):
            if (li[-1] == '{'):
                li.append(i)
                # print("6st If")
                # print(li,total)
            elif (li[-1] == '}' and len(li) > 1):
                total = total + 1
                li.pop()
                li.pop()
                li.append(i)
                # print("7st If")
                # print(li,total)
            elif(li[-1] == '}' and len(li) == 1):
                total = total + 2
                li.pop()
                li.append(i)
        # print("loop")
    if len(li) > 0:
        if(len(li) == 1):
            total = total + 2
            # print("8st If")
            # print(li,total)
        elif(len(li) > 1):
            while(len(li)):
                if(li[-1] == '}'):
                    total = total + 1
                    li.pop()
                    li.pop()
                elif(li[-1] == '{'):
                    total = total + 2
                    li.pop()
            # total = total + 1
    # print("Final")
    print(total)
    T = T - 1