# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
# A (3,6); B (2,1) -> 5,09 // A (7,-5); B (1,-1) -> 7,21

ax = int(input('введите координтау х точки а \n'))
ay = int(input('введите координтау y точки а \n'))
bx = int(input('введите координтау х точки b \n'))
by = int(input('введите координтау y точки b \n'))

distance = (((bx-ax)**2)+((by-ay)**2))**0.5

print(round(distance,2))