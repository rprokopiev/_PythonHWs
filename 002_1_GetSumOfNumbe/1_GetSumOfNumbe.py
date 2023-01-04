# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = input('Enter number\n')
sum = 0
if '.' in a:
    a = a.split('.')
    a = a[0] + a[1]
    for i in range(len(a)):  # можно заменить на "for i in n"
        sum += int(a[i])
    print(sum)
else:
    for i in range(len(a)):  # можно заменить на "for i in n"
        sum += int(a[i])
    print(sum)

# ДР РЕШЕНИЕ
    # summ = 0
    # for i in a:
    #     if i.isdigit():       # проверяем является ли i числом
    #         summ += int(i)
    # print(summ)

# (числами)
n = float(input())
summ = 0
len_num = len(str(n))-1     # переменная для округления до нужного кол-ва знаков (-1 - на точку)
while n != int(n):          # умножаем n на 10 до тех пор пока float(а) = int(a)
    n = round(n*10, len_num)
while n > 0:           
    summ += n % 10  # остаток от деления на 10 приб. к сумме
    n = n // 10     # убираем послед цифру из n.
print(summ)