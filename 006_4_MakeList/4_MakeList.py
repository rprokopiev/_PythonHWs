# Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

n = int(input('enter number - '))
n_list = []

for i in range(0, n):
    if i == 0: n_list.append(1)
    elif i % 2 == 1:
        n_list.append(-(abs(n_list[i-1])*3))
    else:
        n_list.append(abs(n_list[i-1])*3)


print(n_list)
