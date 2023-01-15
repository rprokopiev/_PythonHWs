# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# e.g. 12 => 2, 2, 3. простое число - делится только на себя и один.

# РАЗБОР
import math
n = int(input())
res_list = []
cur_num = 2
while n != 1:
    if n % cur_num == 0:
        res_list.append(cur_num)
        n = n // cur_num
        cur_num = 2
    else:
        cur_num += 1
print(res_list)

# МОЁ
exit()
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
