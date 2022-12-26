# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

n = int(input('Enter number\n'))
i = 1
for x in range(1, n+1):
    print(i*x, end=' ')
    i *= x