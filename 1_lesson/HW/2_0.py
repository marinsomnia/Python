# 2. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа
# сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# in6

# out1 4 1

# in24

# out4 16 4

# in60

# out10 40 10

all_g = int(input())

x = all_g / 3

print(f'{int(x // 2)} {int(x * 2)} {int(x // 2)}')