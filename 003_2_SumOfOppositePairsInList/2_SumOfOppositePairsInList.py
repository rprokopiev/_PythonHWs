# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# print(5%2)
# exit()

def sumListNumbersOppositeIndx(lst):
    lst_sum = []
    y = 1
    if len(lst) % 2 == 1:
        for i in range(0, ((len(lst)//2)+1)):
            lst_sum.insert(i, (lst[i]*lst[len(lst)-y]))
            y += 1
            print(lst_sum)
        return lst_sum
    else:
        for i in range(0, ((len(lst)//2))):
            lst_sum.insert(i, (lst[i]*lst[len(lst)-y]))
            y += 1
            print(lst_sum)
        return lst_sum


list = [5, 1, 3, 3, 6]
print(list)
list_sums = sumListNumbersOppositeIndx(list)
print(list_sums)
