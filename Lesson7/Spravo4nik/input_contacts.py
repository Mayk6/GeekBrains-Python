import csv


def write(list1):
    with open('sw_data_new.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerows([list1])
        print(f'\nКонтакт {" ".join(list1)} успешно добавлен')


def add_contact():
    print("1 - Построчно, 2 - В строку через ';'")
    choice = input('Выберите формат:')
    if choice == "1":
        name = input('Ведите имя:')
        last_name = input('Введите Фамилию:')
        phone = input('Введите телефон:')
        desc = input('Введите описание:')
        return name, last_name, phone, desc
    elif choice == "2":
        inp = input('Введите Имя, Фамилию, Телефон и описание через ",": ')
        list1 = str(inp).split(',')
        return list1[0], list1[1], list1[2], list1[3]
    else:
        print("\nВведен неверный формат")


def contact():
    print("1 - Построчно, 2 - В строку через ','")
    choice = input('Выберите формат:')
    if choice == "1":
        name = input('Ведите имя:')
        last_name = input('Введите Фамилию:')
        return name, last_name
    elif choice == "2":
        inp = input('Введите Имя и Фамилию через ",": ')
        list1 = str(inp).split(',')
        return list1[0], list1[1]
    else:
        print("\nВведен неверный формат")

