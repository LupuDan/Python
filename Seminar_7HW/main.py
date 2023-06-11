# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# def count_syllables(word):
#     vowels = "aeiouаеёиоуыэюя"
#     count = 0
#     for char in word:
#         if char.lower() in vowels:
#             count += 1
#     return count

# def check_rhythm(poem):
#     phrases = poem.split()
#     syllables_count = None
#     for phrase in phrases:
#         words = phrase.split('-')
#         phrase_syllables_count = sum(count_syllables(word) for word in words)
#         if syllables_count is None:
#             syllables_count = phrase_syllables_count
#         elif syllables_count != phrase_syllables_count:
#             return False
#     return True

# poem = input("Введите стихотворение Винни-Пуха: ")
# if check_rhythm(poem):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")



# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            print(result, end='\t')
        print()

# Пример использования
def multiplication(x, y):
    return x * y

print_operation_table(multiplication, num_rows=4, num_columns=4)