# ввод
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
# print(*find_farthest_orbit(orbits))
# вывод
# 2.5 10
# напишите функцию find_farthest_orbit(list_of_orbits), которая найдет найдет ту, по которой вращается самая далекая планета.
# Площадь эллипса S=pi * a * b, где а и в длины полуосей эллипса


def find_farthest_orbit(nums_list):
    return max([(a[0] * a[1], a) for a in nums_list if a[0] != a[1]])[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(*find_farthest_orbit(orbits))
