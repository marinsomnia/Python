# Найдите сумму цифр трехзначного числа.
# in
# 123
# out
# 6

num = int(input())
sum_num = 0
while num > 0:
    x = num % 10
    sum_num = sum_num + x
    num //= 10

print(sum_num)
