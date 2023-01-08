# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random
lst = [1.1, 1.2, 3.1, 5.9, 10.01]
print(lst)

mn = 1
mx = 0
for i in range(0, len(lst)):
    n = round(lst[i] - int(lst[i]), 2)
    if n != 0:
        if round(lst[i] - int(lst[i]), 2) < mn:
            mn = round(lst[i] - int(lst[i]), 2)
        if round(lst[i] - int(lst[i]), 2) > mx:
            mx = round(lst[i] - int(lst[i]), 2)
result = mx - mn
print(result)

# ДР СПОСОБ

# сделали функцию, которай осталяет только дробную часть:


def drob(num):
    return round(num % 1, 2)

    # формируем случайн список из float:
a = [round(random.uniform(0, 10), 2) for i in range(random.randint(5, 8))]
#          uniform - выдаёт случайные floatы
print(a)

# формируем список из дробных частей (e.g. 1,11 => 0,11):
list_drob = list(map(drob, a))
# map - 1й аргумент - применяемая ф-ия,
#       2й арг - к чему эту ф-ию применить.
print(list_drob)
print(min(list_drob), max(list_drob))
print(max(list_drob)-min(list_drob))
