from input_ contacts import *
from output_contacts import *


def start():
    choice = None
    while choice != 0:
        print_menu()
        choice = int(input('Ваш выбор: '))
        if choice == 1:
            read()
        elif choice == 2:
            search_contact(contact())
        elif choice == 3:
            write(add_contact())
        elif choice == 4:
            delete(contact())
        elif 0:
            exit()
