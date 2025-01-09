"""
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""
def reverseString(s):
    if len(s) == 0:
        return s
    else:
        return reverseString(s[1:]) + s[0]
    

if __name__ == '__main__':
    s = input("Digite uma string: ")
    print(reverseString(s))
