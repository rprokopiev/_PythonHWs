# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
a = input('Введите требуемую точность ')
d = 0
for i in range(2,len(a)):
    d += 1
print(round(math.pi,d))

# РАЗБОР
lgth = a.split('.')[1]
print(round(math.pi,len(lgth)))
