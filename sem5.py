
# Словари
# -------
dict = {'apple':'яблоко', 'grape':'виноград'}

# ключами словаря могут быть только неизменяемые типы
# str, int, float, bool, tuple, frozenset

# print(dict['apple'])
# dict['orange'] = 'апельсин'

# some_str = 'привет'
# print(id(some_str))
# some_str += '!'
# print(id(some_str))

# for el in dict:
#     print(el, dict[el])

# for value in dict.values():
#     print(value)

# Задача со скрабблом see homework3
# -------------------
# dict = { frozenset(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']) : 1,
#         frozenset(['D', 'G']) : 2,
#         ...}


# Подсчитать количество букв в строке
# some_dict = {}

# some_str = 'aabc'
# for s in some_str:
#     if s in some_dict:
#         some_dict[s] = some_dict[s] + 1
#     else:
#         some_dict[s] = 1     

# for s in some_dict:
#     value = some_dict[s]
#     if value > 0:
#         print(f'Буква {s} встречается {value} раз')

# def fib(N):
#     return 1 if N<3 else fib(N-1) + fib(N-2)

# Заменить в массиве максимальный элемент на минимальный

# arr = [1,4,3,5,2,3,2];

# max = 0
# min = 5
# for i in range(len(arr)):
#     val = arr[i]
#     if val < min:
#         min = val
#     if val > max:
#         max = val        

# for i in range(len(arr)):
#     if arr[i] == max:
#         arr[i] = min

# print(arr)


# def isSimply(N):
#     i = 2
#     while i < N:
#         if N % i == 0:
#             return False
#         i += 1
#     return True

# for i in range(100):
#     if isSimply(i):
#         print(i)



def f(count):
    if count == 0:
        return 
    else:
        x = int(input('input number: '))
        f(count-1)
        print(x)

f(5)

