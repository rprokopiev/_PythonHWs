# Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

import random
a = [random.randint(1, 10) for i in range(5)]
res = [a[indx]*a[-indx-1] for indx in range(len(a)//2+len(a) % 2)]
print(a)
print(res)

exit()
# MINE


def GetRandList(x, y):
    import random
    lst = [random.randint(1, x) for i in range(0, y)]
    return lst


lst1st = GetRandList(int(input('numbers max value - ')),
                     int(input('list lenght - ')))
print(lst1st)

lst2nd = []
if len(lst1st) % 2 == 1:
    for i in range(0, (len(lst1st)//2) + 1):
        lst2nd.append(lst1st[i]*lst1st[((len(lst1st))-1)-len(lst2nd)])
else:
    for i in range(0, (len(lst1st)//2)):
        lst2nd.append(lst1st[i]*lst1st[((len(lst1st))-1)-len(lst2nd)])

print(lst2nd)
