# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def getRandIntListUserSettings(       # получить список из случайных int чисел с настройками пользователя
        lght=int(input('Введити длинну списка \n')),
        min=int(input('Введити минимальное значение списка \n')),
        max=int(input('Введити максимальное значение списка \n'))):
    if min > max:
        return print('Ошибка')
    else:
        import random
        lst = []
        for i in range(0, lght):
            lst.insert(i, random.randint(min, max))
        return lst

def sumListNumbersOnOddIndx(lst):      # найти сумму элементов списка, стоящих на нечётной позиции
    sum = 0
    for i in range(1, len(lst), 2):
        sum += lst[i]
    return sum


list = getRandIntListUserSettings()
print(list)
print(sumListNumbersOnOddIndx(list))
