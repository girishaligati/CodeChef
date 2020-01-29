#Recursion Programs

#Program to print the text in reverse using recursion
# def rec(word):
#     if(len(word) == 0):
#         return
#     else:
#         rec(word[1:])
#         print(word[0])

# rec('abcd')


def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        print(line)
    return line

print(pascal(6))