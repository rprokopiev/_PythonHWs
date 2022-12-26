# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = input('Enter number\n')
sum = 0
if '.' in a:
    a = a.split('.')
    n = a[0] + a[1]
    for i in range(len(n)):
        sum += int(n[i])
    print(sum)    
else:
    for i in range(len(a)):
        sum += int(a[i])
    print(sum)
