# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Файлы пишем сами.
# e.g. файл 1: 2x**2 + 5 / файл 2: x**3 + 3x + 4 => x**3+2x**2+3x+9

with open('c:/Users/RND/Documents/RP/4.Python/HW/004_5_GetSumFrom2Files/file5_1.txt') as data:
    content = data.readline()
    st = content.split(' + ')
    print(st)

with open('c:/Users/RND/Documents/RP/4.Python/HW/004_5_GetSumFrom2Files/file5_2.txt') as data:
    content = data.readline()
    nd = content.split(' + ')
    print(nd)

result = []
