# Реализуйте алгоритм перемешивания списка

def IntListMixing(lst):
    import random
    randLst = []
    for i in range(0, len(lst)):
        a = random.randint(0, (len(lst)-1))
        randLst.insert(i, lst[a])
        lst.pop(a)
    return randLst


# list = [1, 2, 3, 345, 4, 5, 6, 8, 76]
# list_rand = []
# print(list)
# list_rand = IntListMixing(list)
# print(list_rand)

# РЕШЕНИЕ СПЕЦ Ф-ИИ
#  import random
# a = [1,3,4,5,6,4]
# random.shuffle(a) - спец функция для сучайного перемешивания

# РЕШЕНИЕ С ИМПОРТОМ DATATIME

def random_int(num):
    import datetime
    rand = datetime.datetime.now().microsecond/10**6 # микросекунда, делим на 1млн, т.к. они 6 знаков после заяпятой
    return int(num*rand)
a = [1, 3, 2, 4, 5, 6]
print(a)

for i in range(len(a)-1, -1, -1):
    j = random_int(i+1)
    a[i],a[j]= a[j],a[i]
print(a)