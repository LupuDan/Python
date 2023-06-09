# Напишите такое лямбда-выражение transformation,
# чтобы transformed_values получился копией values.


values = [1, 23, 42, 55]
transformation = lambda i: i
transformed_values = list(map(transformation, values))
print(f"or: {values}")
print(f"co: {transformed_values}")

if values == transformed_values:
    print('ok')
else:
    print('fail')