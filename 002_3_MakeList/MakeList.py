# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму

length = int(input('Enter number\n'))
sch = []
x = float(1)
amount = float(0)

for i in range(0, length):
    sch.insert(i, round(((1+(1/x))**x), 2))
    amount += sch[i]
    x += 1
print(sch)
print(amount)

# СПОСОБ СЛОВАРЁМ
n = int(input('Enter number\n'))
dict_num = {}               # объявление словаря
for i in range(1, n+1):
    dict_num[i] = round(((1 + (1/i))**i),2)
print(dict_num)
print(sum(dict_num.values()))
