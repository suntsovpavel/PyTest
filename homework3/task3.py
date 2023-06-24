# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12


# Возвращаем очко для одной буквы
def valueLetter(x):
    x = x.lower()
    # Английские буквы
    if x in 'AEIOULNSTR'.lower():
        return 1
    if x in 'DG'.lower():
        return 2
    if x in 'BCMP'.lower():
        return 3
    if x in 'FHVWY'.lower():
        return 4
    if x == 'k':
        return 5
    if x in 'JX'.lower():
        return 8
    if x in 'QZ'.lower():
        return 10
    # Русские буквы
    if x in 'АВЕИНОРСТ'.lower():
        return 1
    if x in 'ДКЛМПУ'.lower():
        return 2    
    if x in 'БГЁЬЯ'.lower():
        return 3
    if x in 'ЙЫ'.lower():
        return 4
    if x in 'ЖЗХЦЧ'.lower():
        return 5   
    if x in 'ШЭЮ'.lower():
        return 5   
    if x in 'ФЩЪ'.lower():
        return 5   

word = input('Введите слово: ')
# Суммируем осчки по буквам 
sum=0
for letter in word:
    sum += valueLetter(letter)
print(f'Сумма очков: {sum}')