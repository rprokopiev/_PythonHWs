# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

import random

k = int(input('Введите K \n'))

path = 'c:/Users/RND/Documents/RP/4.Python/HW/004_4_WritePolynominalToFile/file4.txt'
data = open(path, 'w')

while k >= 0:
    if k == 0:
        data.write(str(random.randint(0, 100)))
        data.write(' = 0')
        k -= 1
    elif k == 1:
        data.write(str(random.randint(0, 100)))
        data.write('x')
        data.write(' + ')
        k -= 1
    else:
        data.write(str(random.randint(0, 100)))
        data.write('x**')
        data.write(str(k))
        data.write(' + ')
        k -= 1

data.close()
