# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Файлы пишем сами.
# e.g. файл 1: 2x**2 + 5 / файл 2: x**3 + 3x + 4 => x**3+2x**2+3x+9

# РАЗБОР
pol1 = '4*x**3 + 2*x**2 + 5'
pol2 = '1*x**3 + 3*x**1 + 4'
# избавляемся от плюсов
pol1 = pol1.split('+')
pol2 = pol2.split('+')
print(pol1)
print(pol2)
# из аргументов типа 4*x**3 получем [4,3]
for indx, value in enumerate(pol1):
    pol1[indx] = list(map(int, (value.split('*x**'))))
for indx, value in enumerate(pol2):
    pol2[indx] = list(map(int, (value.split('*x**'))))
print(pol1)
print(pol2)

result_pol = pol1 + pol2
print(result_pol)

polyn_dict = {}
for value in result_pol:
    if len(value) > 1:
        if value[1] in polyn_dict.keys():
            polyn_dict[value[1]] += value[0]
        else:
            polyn_dict[value[1]] = value[0]
    else:
        if 0 in polyn_dict.keys():
            polyn_dict[0] += value[0]
        else:
            polyn_dict[0] = value[0]

print(polyn_dict)
print(polyn_dict.items())

result_pol = dict(sorted(polyn_dict.items()))
print(result_pol)
finish_line = ''
for stepen, koeff in result_pol.items():
    if stepen >1:
        finish_line += f'{koeff}*x**{stepen}+'
    if stepen == 0:
        finish_line += f'{koeff}'
print(finish_line)

exit()
with open('c:/Users/RND/Documents/RP/4.Python/HW/004_5_GetSumFrom2Files/file5_1.txt') as data:
    content = data.readline()
    st = content.split(' + ')
    print(st)

with open('c:/Users/RND/Documents/RP/4.Python/HW/004_5_GetSumFrom2Files/file5_2.txt') as data:
    content = data.readline()
    nd = content.split(' + ')
    print(nd)

result = []
