# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

from turtle import distance


x1 = int(input('введите координату X первой точки => '))
y1 = int(input('введите координату Y первой точки => '))
x2 = int(input('введите координату X второй точки => '))
y2 = int(input('введите координату Y второй точки => '))

line_x = x2 - x1
line_y = y2 - y1
result = (line_x**2 + line_y**2) ** 0.5
print(round(result, 2))