# Функция для последней задачи
# def fibonacci(numb):
#     if numb in (1, 2):
#         return 1
#     return fibonacci(numb - 1) + fibonacci(numb - 2)

# Задайте список из нескольких   чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# list1 = [2, 3, 5, 9, 3]
# i = 0
# summ = 0
# while i < len(list1):
#     if i % 2 != 0:
#         summ += list1[i]
#     i = i + 1
# print(summ)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# list1 = [2, 3, 4, 5, 6]
# list2 = []
# i = 1
# multiply = 0
# while i < len(list1)/2+1:
#     list2.append(list1[i-1] * list1[-i])
#     i = i + 1
# print(list2)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# list1 = [1.1, 1.2, 3.1, 5, 10.01]
# list2 = []
# for i in list1:
#     if i % 1 != 0:
#         list2.append(round(i % 1, 2))
# print(max(list2) - min(list2))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# result = ""
# number = int(input("Введите число: "))
# while number != 0:
#     result = str(number % 2) + result
#     number = number // 2
# print(result)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# list1 = [0]
# number = int(input("Введите желаемое число : "))
# for i in range(1, number + 1):
#     list1.append(fibonacci(i))
#     list1.insert(0, ((-1) ** (i + 1)) * fibonacci(i))
# print(list1)
