# 33.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

   # 8
   # 5 4 2 2 4 2 2 5

def max_to_min(list):
    mini = min(list)
    maxi = max(list)
    return [mini if i == maxi else i for i in list]
print(*max_to_min([int(i) for i in input().split()]))
