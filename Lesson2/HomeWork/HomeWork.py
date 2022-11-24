#     Напишите программу, которая  принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11
# number = input()
# sum_numb = 0
# i = 0
# while i < len(number):
#     if number[i] == ',' or number[i] == '.':
#         i = i+1
#     else:
#         sum_numb = sum_numb + int(number[i])
#         i = i+1
# print(sum_numb)
import random

#     Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# number = int(input())
# product_numb = 1
# list1 = []
# for i in range(1, number+1):
#     product_numb *= i
#     list1.append(product_numb)
# print(list1)

#     Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# n = int(input('Введите кол-во элементов последовательности: '))
# a = []
# summ = 0
# for i in range(1, n+1):
#     b = (1 + 1 / i) ** i
#     summ = summ + b
#     a.append(round(b, 2))
# print('{', end='')
# print(*a, sep=',', end='')
# print('}')
# print('Сумма',round(summ, 2))

# *4. НЕОБЯЗАТЕЛЬНАЯ ЗАДАЧА
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# number = int(input())
# i = 0
# list1 = []
# list2 = []
# product_num = 1
# while i < number:
#     list1.append(random.randint(-number, number))
#     i += 1
# print(list1)
# with open('file.txt', 'w', encoding='utf-8') as f:
#     for b in range(0, number - 2):
#         r = random.randint(0, number-1)
#         f.write(str(r))
#         f.write("\n")
# with open('file.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()
#     while line:
#         print(line)
#         list2.append(int(line.strip()))
#         line = f.readline()
# for i in list2:
#     product_num *= list1[i]
# print(product_num)

#     Реализуйте алгоритм перемешивания списка.
# list1 = [1, 3, 6, 8, 95, 453, 3, 245]
# i = 0
# while i < len(list1):
#     r = random.randint(0, len(list1)-1)
#     temp = list1[i]
#     list1[i] = list1[r]
#     list1[r] = temp
#     i = i+1
# print(list1)

#     ДОП. задача на алгоритмы с реальных собеседований
#     Даны два массива:
#     [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
#     Надо вернуть их пересечение
#     [1, 2, 2, 3]
#     (порядок не важен)
# list1 = [1, 2, 3, 2, 0]
# list2 = [5, 1, 2, 7, 3, 2]
# list3 = []
# for i in list1:
#     for j in list2:
#         if i == j:
#             list3.append(i)
#             break
# print(list3)


