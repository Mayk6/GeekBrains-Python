# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут  температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!
import re


def get_sign(char):
    if char[0] in '+':
        return char[0]


list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(list1):
    char = get_sign(list1[i])
    if list1[i].isdigit() or (char and list1[i][1:].isdigit()):
        if char:
            list1[i] = char + list1[i][1:].zfill(2)
        else:
            list1[i] = list1[i].zfill(2)
        list1[i] = f'"{list1[i]}"'
    i += 1
print(" ".join(list1))


# print(" ".join(map(lambda a: '"%s"' % re.sub('\d+', lambda a: f'{a[0]}'.zfill(2), a) if any(map(str.isdigit, a)) else a, list1)))


# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


def BreakTheNumber(a):
    a = str(a).split('.')
    if len(a) > 1:
        return f'{a[0]} руб {a[1].zfill(2)} коп'
    else:
        return f'{a[0]} руб 00 коп'


price = [57.8, 46.51, 97, 20.45, 69.47, 32.15, 45, 89, 150, 63.87, 118, 589.45, 123, 183, 152.13, 504, 985, 145, 588]
print(list(map(BreakTheNumber, price)))
price.sort()
print(list(map(BreakTheNumber, price)))
pricedown = price
pricedown.sort(reverse=True)
print(list(map(BreakTheNumber, pricedown)))
print(list(map(BreakTheNumber, pricedown[0:5])))


# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Известно, что имя сотрудника всегда в конце строки.
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?


def find_name(a):
    a = a.split()
    return a[len(a) - 1].title()


employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

for i in employees:
    print(f'Привет, {find_name(i)}!')

print(list(map(find_name, employees)))