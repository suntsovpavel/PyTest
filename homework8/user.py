
def choose_mode():
    mode = input('Введите режим работы: запись, поиск, изменение, удаление: ')
    person = {}
    keyword = ''  # слово поиска (имя или фамилия)
    if mode == 'запись':
        person = fill_person()
    elif mode == 'поиск' or mode == 'изменение' or mode == 'удаление':
        keyword = input('Введите имя или фамилию человека: ')
    else:
        print('Введен некорректный режим')
        choose_mode()
    return person, mode, keyword

def fill_person():
    dict_user = {}
    dict_user['surname'] = input('Введите фамилию: ')
    dict_user['name'] = input('Введите имя: ')
    dict_user['second_name'] = input('Введите отчество: ')
    dict_user['phone'] = input('Введите телефон: ')
    return dict_user
