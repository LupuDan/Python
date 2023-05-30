# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# s = input().split()
# result = {}
# for n in s:
#     if n in result:
#         print(f'{n}_{result[n]}', end=' ')
#     else:
#         print(n, end=' ')
#     result[n] = result.get(n, 0) + 1


# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним
# или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore
# The shells that she sells are sea shells
# I'm sure.So if she sells sea shells on
# the sea shore I'm sure that the
# shells are sea shore shells

print(len(set(input().lower().split())))