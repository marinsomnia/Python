# Задача №1461. Шарики
# В одной компьютерной игре игрок выставляет в линию шарики разных цветов.
# Когда образуется непрерывная цепочка из трех и более шариков одного цвета,
# она удаляется из линии.
# Все шарики при этом сдвигаются друг к другу, и ситуация может повториться.
# Напишите программу, которая по данной ситуации определяет, сколько шариков
# будет "уничтожено".
# Естественно, непрерывных цепочек из трех и более одноцветных шаров в начальный момент
# может быть не более одной.
# Входные данные
# A
# Сначала вводится количество шариков в цепочке (не более 1000) и
# цвета шариков (от 0 до 9, каждому цвету соответствует свое целое число).
# о
# Ө
# Выходные данные
# Требуется вывести количество шариков, которое будет "уничтожено".
# Примеры
# входные данные
# 5 1 3 3 3 2
# выходные данные
# 3
# 1 1 2 3 4 5 5 5 6 7 8 8 8 4 2 2 2 2 2

from itertools import groupby

res_list = [len(list(v)) for ch, v in groupby(input().split())]
print(sum([i for i in res_list if i > 2]))