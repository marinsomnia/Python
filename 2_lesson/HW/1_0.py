# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2

n = int(input())
up = down = 0
for _ in range(n):
    count = int(input())
    if count:
        up += 1
    else:
        down += 1
if up > down:
    print(down)
else:
    print(up)
