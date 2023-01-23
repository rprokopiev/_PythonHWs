# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
# A (3,6); B (2,1) -> 5,09 // A (7,-5); B (1,-1) -> 7,21

a = [int(input(f'enter {i} of a ')) for i in 'xy']
b = [int(input(f'enter {i} of b ')) for i in 'xy']
res = sum([(element[1] - element[0])**2 for element in zip(a,b)])**0.5
print(res)

exit()
# MINE
ax = int(input('введите координтау х точки а \n'))
ay = int(input('введите координтау y точки а \n'))
bx = int(input('введите координтау х точки b \n'))
by = int(input('введите координтау y точки b \n'))

distance = (((bx-ax)**2)+((by-ay)**2))**0.5

print(round(distance,2))