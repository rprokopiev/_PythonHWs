# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

path = 'c:/Users/RND/Documents/RP/4.Python/HW/002_4_SumPerFile/file.txt'
        # ИСТПРАВИТЬ НА ФАКТИЧЕСОЕ РАСПОЛОЖЕНИЕ ФАЙЛА. 
data = open(path, 'r')
file = []
m = 0
for line in data:
    file.insert(m, int(line))
    m += 1
print('list from file: ', file)
data.close()

n = int(input('Enter number\n'))
l = -n
lst = []
x = 0
while l <= n:
    lst.insert(x, l)
    x += 1
    l += 1
print('list between -N and N: ', lst)

amount = 1
for y in range(0, len(file)):
    amount *= lst[file[y]]
print(amount)
