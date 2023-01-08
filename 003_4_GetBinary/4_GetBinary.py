# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def dec_to_bin(num, result = ''):
    if num == 0:
        return result
    result = str(num%2) + result
    return dec_to_bin(num // 2, result)
print(dec_to_bin(int(input())))
print(bin(int(input()))) # ф-ия перевода в двоичное, результат начинается с 0b...
print(bin(int(input()))[2::]) # то же самое без 0b...

#МОЁ
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
