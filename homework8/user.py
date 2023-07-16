
def choose_mode():
    mode = input('Введите режим работы: запись, поиск, изменение, удаление: ')
    person = {}
    keyword = ''
    if mode == 'запись':
        person = fill_person()
    elif mode == 'поиск' or mode == 'изменение' or mode == 'удаление':
        keyword = input('Введите имя или фамилию человека: ')
    else:
        print('Введен некорректный режим')
        choose_mode()
    return person, mode, keyword


def fill_person():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    second_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    return {'surname': surname, 'name': name, 'second_name': second_name, 'phone': phone}
