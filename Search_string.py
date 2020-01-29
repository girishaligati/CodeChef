class StringHandling():
    def __init__(self):
        self.input_string = input("Enter the string - ")
        self.word = input("Enter the word that has to be replaced in the string - ") 
        self.new_word = input("Enter the new word - ")
    
    def SearchWord(self):
        N = len(self.input_string)
        len_word = len(self.word)
        li = list(self.input_string)
        # flag = -1?
        for i in range(N):
            if (self.word[0] == li[i]):
                k = 0
                while(k < len_word and self.word[k] == li[i+k]):
                    # print("in while",self.word[k],li[k+i])
                    k = k + 1
                if(k == (len_word)):
                    # print("Found string in the list")
                    return 0
                else:
                    return -1
                    

    
    def replace_word(self):
        N = len(self.input_string)
        len_word = len(self.word)
        li = list(self.input_string)
        result = []
        i = 0
        while i < N:
            # print(i)
            if (self.word[0] == li[i]):
                k = 0
                while(k < len_word and self.word[k] == li[i+k]):
                    # print("in while",self.word[k],li[k+i])
                    k = k + 1
                if(k == (len_word)):
                    # print("Found string in the list")
                    result.append(self.new_word)
                    # result.append(li[i:k])
                i = i + k
                # print('in if', i,k)
            else:
                result.append(li[i])
                i = i + 1
        return(''.join(result))



if __name__ == "__main__":
    obj = StringHandling()
    print(obj.SearchWord())
    print(obj.replace_word())
