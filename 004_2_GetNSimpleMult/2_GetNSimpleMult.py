# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# e.g. 12 => 2, 2, 3. простое число - делится только на себя и один.
import math
n = int(input('Введите число \n'))
x = n
primeIntList = []
for i in range(2, (int(n/2))):
    while x % i == 0:
        x //= i
        primeIntList.append(i)
else:
    primeIntList.append(n)
print(primeIntList)