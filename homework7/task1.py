# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

vowel_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

# Эта функция считает количество гласных в строке 
def count_vowel_letters_in_line(s: str):
    result = 0
    for letter in s:
        if letter in vowel_letters:
            result += 1
    return result

poem = input('Введите стихотворение: ')
# for test:
# poem = 'Серый-зайка-вырвал-травку Положил-её-на-лавку'

# 1. Разбиваем поэму на строки
strings = [x for x in poem.split(' ') if len(x)>0]

# 2. В каждой строке считаем количество гласных
# Формируем список количества гласных по строкам
count_vowel_letters = [count_vowel_letters_in_line(s) for s in strings]
print(f'Количество гласных по строкам: {count_vowel_letters}')

# Преобразуем список в множество. 
# Если количество гласных во всех строках одно и то же, 
# получим множество, состоящее из одного элемента
vowel_letters_set = set(count_vowel_letters) 
if len(vowel_letters_set) == 1:    
    print('Парам пам-пам (с ритмом все в порядке)')
else:
    print('Пам парам (с ритмом все не в порядке)')   





