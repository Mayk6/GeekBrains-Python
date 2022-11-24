# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# text = input()
# text = text.split()
# new_text = list(filter(lambda i: 'abc' not in i, text))
# print(new_text)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# text = "abbaaaarrrreewww"
# new_text = ''
# i = 0
# while i < len(text):
#     count = 1
#     while i + 1 < len(text) and text[i] == text[i + 1]:
#         count += 1
#         i += 1
#     new_text += str(count) + text[i]
#     i = i + 1
# print(new_text)

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random
# all_candys = 2021
# p1_candys = 0
# p2_candys = 0
# p1_get = 0
# p2_get = 0
# while all_candys > 1:
#     while True:
#        p1_get = int(input('Игрок 1: '))
#        if p1_get <= 28 and p1_get > 0 and p1_get <= all_candys:
#            p1_candys += p1_get
#            if all_candys - p1_get == 0:
#                print('Игрок 1 победил')
#                exit()
#            all_candys -= p1_get
#            print(f'у игрока 1 всего {p1_candys} конфет')
#            p1_get = 0
#            break
#        else:
#            print('Вы не можете взять  конфет больше чем 28 и меньше чем 1 или на столе осталось меньше конфет.')
#     while True:
#        p2_get = int(input('Игрок 2: '))
#        if p2_get <= 28 and p2_get > 0 and p2_get <= all_candys:
#            p2_candys += p2_get
#            if all_candys - p2_get == 0:
#                print('Игрок 2 победил')
#                exit()
#            all_candys -= p2_get
#            print(f'у игрока 2 всего {p2_candys} конфет')
#            p2_get = 0
#            break
#        else:
#            print('Вы не можете взять конфет больше чем 28 и меньше чем 1 или на столе осталось меньше конфет.')
#     print(f'на столе осталось {all_candys} конфет')

# Создайте программу для игры в ""Крести
# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
#
# board = list(range(1,10))
#
# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)
#
# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")
#
# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)
#
# input("Нажмите Enter для выхода!")
