# Реализуйте алгоритм перемешивания списка
def IntListMixing(lst):
    import random
    randLst = []
    for i in range(0, len(lst)):
        a = random.randint(0, (len(lst)-1))
        randLst.insert(i, lst[a])
        lst.pop(a)
    return randLst

list = [1, 2, 3, 345, 4, 5, 6, 8, 76]
list_rand = []
print(list)
list_rand = IntListMixing(list)
print(list_rand)

