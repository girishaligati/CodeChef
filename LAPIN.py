T = int(input())
while (T>0):
    word = input()
    arr=[0]*26
    half = int(len(word)/2)
    for i in range(half):
        if(len(word) % 2 == 0 ):
            arr[ord(word[i]) - ord('a')] = arr[ord(word[i])-ord('a')] + 1
            # print(arr)
            arr[ord(word[i+half]) - ord('a')] = arr[ord(word[i+half]) - ord('a')] - 1
            # print(arr)
        else:
            arr[ord(word[i]) - ord('a')] = arr[ord(word[i])-ord('a')] + 1
            arr[ord(word[i+half+1]) - ord('a')] = arr[ord(word[i+half+1]) - ord('a')] - 1
    if ([0]*26 == arr):
        print("YES")
    else:
        print("NO")
    T = T - 1