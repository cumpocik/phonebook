def show_menu():
    print('1. Распечатать справочник.',
    '2. Найти телефон по фамилии.',
    '3. Изменить данные.',
    '4. Удалить запись.',
    '5. Найти абонента по номеру телефона.',
    '6. Добавить абонента в справочник.',
    '7. Копирование данных из одного файла в другой.',
    '8. Закончить работу.', sep = '\n')
    choice = int(input('Введите номер команды: '))
    return choice
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phone.txt')
    while (choice != 8):
        if choice == 1:
            for contact in phone_book:
                print(contact['Фамилия'], contact['Имя'], contact['Телефон'], contact['Описание'])
            choice = show_menu()
        elif choice == 2:
            find_by_lastname(phone_book)
        elif choice == 3:
            print('1. Изменить фамилию.',
            '2. Изменить имя.',
            '3. Изменить телефон.',
            '4. Вернуться назад.', sep = '\n')
            choice = int(input('Введите номер команды: '))
            if choice == 1:
                print(change_lastname(phone_book))
            elif choice == 2:
                print(change_name(phone_book))
            elif choice == 3:
                print(change_number(phone_book))
            elif choice == 4:
                work_with_phonebook()
        elif choice == 4:
            print(delete_by_lastname(phone_book))
        elif choice == 5:
            print(find_by_number(phone_book))
        elif choice == 6:
            add_user(phone_book)
        elif choice == 7:
            copypast(phone_book)
    choice = show_menu()
def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book
def write_txt(filename, phone_book):
        with open(filename, 'w', encoding = 'utf-8') as phout:
            for i in range(len(phone_book)):
                s = ''
                for j in phone_book[i].values():
                    s += j + ','
                phout.write(f'{s[:-1]}\n')
def find_by_lastname(phone_book):
    print('Введите фамилию контакта: ')
    lastname = input()
    for contact in phone_book:
        if contact['Фамилия'] == lastname:
            print(contact['Телефон'])
            break
    else:
        print('Контакт не найден.')
    work_with_phonebook()
def change_number(phone_book):
    print('Введите фамилию контакта: ')
    lastname = input()
    for contact in phone_book:
        if contact['Фамилия'] == lastname:
            print('Текущий номер: ', contact['Телефон'])
            print('Введите новый номер: ')
            new_number = input()
            contact['Телефон'] = new_number
            write_txt('phone.txt', phone_book)
            print('Номер успешно сохранен.')
            break
    else:
        print('Контакт не найден.')
    work_with_phonebook()
def change_lastname(phone_book):
    print('Введите номер контакта: ')
    number = input()
    for contact in phone_book:
        if contact['Телефон'] == number:
            print('Текущая фамилия: ', contact['Фамилия'])
            print('Введите новую фамилию: ')
            new_lastname = input()
            contact['Фамилия'] = new_lastname
            write_txt('phone.txt', phone_book)
            print('Фамилия успешно сохранена.')
            break
    else:
        print('Контакт не найден.')
    work_with_phonebook()
def change_name(phone_book):
    print('Введите фамилию контакта: ')
    lastname = input()
    for contact in phone_book:
        if contact['Фамилия'] == lastname:
            print('Текущее имя: ', contact['Имя'])
            print('Введите новое имя: ')
            new_name = input()
            contact['Имя'] = new_name
            write_txt('phone.txt', phone_book)
            print('Имя успешно сохранено.')
            break
    else:
        print('Контакт не найден.')
    work_with_phonebook()
def delete_by_lastname(phone_book):
    print('Введите фамилию контакта: ')
    lastname = input()
    for contact in phone_book:
        if contact['Фамилия'] == lastname:
            phone_book.remove(contact)
            write_txt('phone.txt', phone_book)
            print('Контакт удален.')
            break
    else:
        print('Контакт не найден.')
    work_with_phonebook()
def find_by_number(phone_book):
    print('Введите номер контакта: ')
    number = input()
    for contact in phone_book:
        if contact['Телефон'] == number:
            print('Данные контакта: ', contact['Фамилия'], contact['Имя'], contact['Описание'])
            break
    else:
        print('Контакт не найден.')
    work_with_phonebook()
def add_user(phone_book):
    print('Введите фамилию нового контакта: ')
    user_lastname = input()
    print('Введите имя нового контакта: ')
    user_name = input()
    print('Введите телефон нового контакта: ')
    user_phone = input()
    print('Введите описание нового контакта: ')
    user_desc = input()
    new_contact = {
       'Фамилия' : user_lastname,
       'Имя' : user_name,
       'Телефон' : user_phone,
       'Описание' : user_desc
    }
    phone_book.append(new_contact)
    write_txt('phone.txt', phone_book)
    print('Контакт сохранен.')
    work_with_phonebook()
def copypast(phone_book):
    print('Введите путь к файлу, в который нужно добавить данные: ')
    way = input('')
    print('Введите порядковый номер контакта из справочника(номер строки): ')
    order = int(input())
    if phone_book[order - 1]:
        with open(way, 'a', encoding = 'utf-8') as phout:
            s = ''
            for j in phone_book[order - 1].values():
                s += j + ','
            phout.write(f'{s[:-1]}\n')
            print('Данные добавлены.')
    else:
        print('Контакт не найден.')
    work_with_phonebook()
work_with_phonebook()
