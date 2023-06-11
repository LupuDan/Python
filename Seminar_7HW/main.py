# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

def count_syllables(word):
    vowels = "aeiouаеёиоуыэюя"
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

def check_rhythm(poem):
    phrases = poem.split()
    syllables_count = None
    for phrase in phrases:
        words = phrase.split('-')
        phrase_syllables_count = sum(count_syllables(word) for word in words)
        if syllables_count is None:
            syllables_count = phrase_syllables_count
        elif syllables_count != phrase_syllables_count:
            return False
    return True

poem = input("Введите стихотворение Винни-Пуха: ")
if check_rhythm(poem):
    print("Парам пам-пам")
else:
    print("Пам парам")