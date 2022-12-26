# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Enter number\n'))
l = -n
lst = []
x = 0
while l <= n:
    lst.insert(x, l)
    x += 1
    l += 1
print(lst)

# amount = 1
# for x in range(0, 2):
    
#     amount *= lst[__file__(1)]

# print(amount)
