# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между ними 
# в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

a_x = int(input('Введите X для точки A: '))
a_y = int(input('Введите Y для точки A: '))
b_x = int(input('Введите X для точки B: '))
b_y = int(input('Введите Y для точки B: '))


distance = str(((a_x - b_x) * (a_x - b_x) + (a_y - b_y) * (a_y - b_y)) ** 0.5).split('.')
print(distance[0] + '.' + distance[1][:2])