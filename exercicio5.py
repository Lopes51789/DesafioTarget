def reverseString(s):
    if len(s) == 0:
        return s
    else:
        return reverseString(s[1:]) + s[0]
    

if __name__ == '__main__':
    s = input("Digite uma string: ")
    print(reverseString(s))
