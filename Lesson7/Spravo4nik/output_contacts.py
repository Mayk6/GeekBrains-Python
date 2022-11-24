import csv
import os
import re
import shutil

from input_contacts import *
head = ['name', 'sure_name', 'phone', 'desc']

def print_menu():
    print("\n" + 'Это главное меню телефонной книги\n',
          'Выберите необходимое действие\n',
          '1 - Вывести на экран всю телефонную книгу\n',
          '2 - Поиск контакта\n',
          '3 - Добавить контакт\n',
          '4 - Удалить контакт\n',
          '0 - Завершить работу с программой')


def read():
    with open('sw_data_new.csv', 'r') as f:
        reader = csv.reader(f)
        print('Выберите формат вывода\n',
              '1 - В одной строке все данные одного контакта',
              '2 - Все контакты в одну строку разделенные ;')
        choice = input('Ваш выбор: ')
        while choice != 0:
            if choice == '1':
                choice = 0
                print()
                for row in reader:
                    print(', '.join(row))
            if choice == '2':
                choice = 0
                print()
                for row in reader:
                    if row == head:
                        continue
                    print(','.join(row) + ';', end='')
                print()

def search_contact(list1=None):
    if list1 is None:
        return

    with open('sw_data_new.csv', 'r') as f:
        reader = csv.reader(f)
        r = 0
        for row in reader:
            i = 0
            while i < len(row):
                if row[i] == list1[0] and row[i + 1] == list1[1]:
                    r = 1
                    print("\nКонтакт найден: " + ', '.join(row))
                    return row
                i += 1
    if r == 0:
        print('\nТакого контакта нет')


def delete(list1=None):
    if list1 is None:
        return
    with open('sw_data_new.csv') as f:
        lines = f.readlines()
    pattern = re.compile(re.escape(list1[0] + ',' + list1[1]))
    print(pattern)
    with open('sw_data_news.csv', 'w') as f:
        for line in lines:
            print(line)
            result = pattern.search(line)
            if result is None:
                f.write(line)
            else:
                print(line)
        print(f'Контакт {",".join(list1)}')
    shutil.move('sw_data_news.csv', 'sw_data_new.csv')
