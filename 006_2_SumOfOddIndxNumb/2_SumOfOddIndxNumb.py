# Найти сумму чисел списка стоящих на нечетной позиции
def GetRandList(x, y):
    import random
    lst = [random.randint(1, x) for i in range(0, y)]
    return lst

lst = GetRandList(int(input('max value \n')), int(input('list lenght \n')))
print(lst)
oddIndNumbSum = 0
for i in range(0, len(lst)):
    if i % 2 == 1: oddIndNumbSum += lst[i]
print(oddIndNumbSum)