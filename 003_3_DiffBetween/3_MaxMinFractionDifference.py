# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list = [1.1, 1.2, 3.1, 5.9, 10.01]
print(list)

min = 1
max = 0
for i in range(0, len(list)):
    n = round(list[i] - int(list[i]), 2) 
    if n != 0:
        if round(list[i] - int(list[i]), 2) < min:
            min = round(list[i] - int(list[i]), 2)
        if round(list[i] - int(list[i]), 2) > max:
            max = round(list[i] - int(list[i]), 2)
result = max - min
print(result)