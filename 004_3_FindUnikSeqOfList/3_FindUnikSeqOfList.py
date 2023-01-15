# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# e.g. дан список 2, 2, 3, 4, 4 => 3
n = [2, 2, 3, 4, 4, 5, 5, 3, 0]
n_unique = []

# РАЗБОР
for i in n:
    if n.count(i) == 1:
        n_unique.append(i)
print(n_unique)

exit()
for i in range(0, len(n)):
    l = 0
    for j in range(0, len(n)):
        if i != j:
            if n[i] == n[j]:
                l += 1
    if l == 0:
        n_unique.append(n[i])

if len(n_unique) > 0:
    print(n_unique)
else:
    print('No unique items ')
