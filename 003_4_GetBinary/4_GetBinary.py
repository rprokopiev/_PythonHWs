# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def getReverseBinary(n):
    if n == 0:
        return 0
    else:
        return str(n % 2) + str(getReverseBinary(n//2))

def revertString(n):
    reverted_n = ''
    y = 0
    for i in range(len(n)-1, -1, -1):
        reverted_n += n[i]
        y += 1
    return reverted_n

decimal = int(input('Enter \n'))
binary = revertString(getReverseBinary(decimal))
print(binary)
