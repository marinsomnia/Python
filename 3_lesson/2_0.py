# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
#  на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

list_nums = [1, 2, 3, 4, 5]

k = 7
print(list_nums)
# result = list_nums[(k % len(list_nums)):] + list_nums[:(k % len(list_nums))]
# print(result)


for i in range(k - 1):
    list_nums.insert(0, list_nums.pop(- 1))

print(k, list_nums)