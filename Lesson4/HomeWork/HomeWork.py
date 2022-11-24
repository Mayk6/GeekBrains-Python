#     Вычислить число c заданной точностью d
# number = float(input('Введите число: '))
# accuracy = input('Введите точность: ')
# if len(accuracy) <= 1:
#     print('Нужно ввести дробное число')
#     exit()
# result = 0
# result = round(number, len(accuracy) - 2)
# print(result)

#     Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# number = int(input())
# list1 = []
# for i in range(1, number):
#     if number % i == 0 and i != number and i % 2 != 0:
#         list1.append(i)
# print(list1)

#     Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# list1 = (map(int, input('Введите последовательность через пробел: ').split()))
# print(set(list1))

#     Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# from random import randint
# import itertools
#
# k = int(input('Введите натуральное число: '))
#
#
# def relation(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios
#
#
# def polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')
#
#
# rela = relation(k)
# result = polynomial(k, rela)
# print(result)
# with open('Result.txt', 'w') as res:
#     res.write(result)

