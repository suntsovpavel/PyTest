# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

def task():
    N = int(input('Введите число N: '))
    value = 1
    while(value <= N):
        print(value)
        value *= 2

task()