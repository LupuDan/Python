# Напишите такое лямбда-выражение transformation,
# чтобы transformed_values получился копией values.


# values = [1, 23, 42, 55]
# transformation = lambda i: i
# transformed_values = list(map(transformation, values))
# print(f"or: {values}")
# print(f"co: {transformed_values}")

# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')



# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.

def find_farthest_orbit(array):
    max_sq = [(i[0] * i[1], i) for i in array if i[0] !=i[1]]
    return max(max_sq)[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(*find_farthest_orbit(orbits))

