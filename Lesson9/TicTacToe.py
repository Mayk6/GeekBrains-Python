class TicTacToeBoard:
    board = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]

    def __init__(self):
        self.who_move = 'X'
        self.game_done = False
        self.board = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]]

    def new_game(self):
        self.__init__()

    def get_field(self):
        return self.board

    def check_field(self):
        diag_left = True
        diag_right = True
        not_finish = False
        win = False
        for i in range(len(self.board)):
            rows_a = 0
            cols_a = 0
            diag_left &= (self.board[i][i] == self.who_move)
            diag_right &= (self.board[len(self.board) - i - 1][i] == self.who_move)
            for j in range(len(self.board)):
                if self.board[i][j] == self.who_move:
                    cols_a += 1
                if self.board[j][i] == self.who_move:
                    rows_a += 1
                if self.board[i][j] == '-':
                    not_finish = True
            if cols_a > 2 or rows_a > 2:
                win = True
        if diag_right or diag_left or win:
            return self.who_move
        elif not_finish:
            return None
        else:
            return "D"

    def change_step(self):
        if self.who_move == 'X':
            self.who_move = '0'
        else:
            self.who_move = 'X'

    def make_move(self, row, col):
        if self.game_done:
            return 'Игра уже завершена'
        if self.check_field() is None and self.board[row - 1][col - 1] == "-":
            self.board[row - 1][col - 1] = self.who_move
            if self.check_field() == "0" or self.check_field() == "X":
                self.game_done = True
                return f"Победил игрок {self.who_move}"
            self.change_step()
            if self.check_field() == 'D':
                self.game_done = True
                return 'Ничья'
            return 'Продолжаем играть'
        elif (self.board[row - 1][col - 1] == 'X' or '0') and (self.check_field() is None):
            return f'Клетка {row, col} уже занята'


b1 = TicTacToeBoard()
print(*b1.get_field(), sep="\n")
print(b1.make_move(1, 1))
print(*b1.get_field(), sep="\n")
print(b1.make_move(1, 1))
print(b1.make_move(1, 2))
print(*b1.get_field(), sep="\n")
print(b1.make_move(2, 1))
print(b1.make_move(2, 2))
print(b1.make_move(3, 1))
print(b1.make_move(2, 2))
print(*b1.get_field(), sep="\n")

b2 = TicTacToeBoard()
print(*b2.get_field(), sep="\n")
print(b2.make_move(1, 2))
print(*b2.get_field(), sep="\n")
print(b2.make_move(1, 1))
print(b2.make_move(1, 3))
print(*b2.get_field(), sep="\n")
print(b2.make_move(2, 2))
print(b2.make_move(2, 3))
print(b2.make_move(3, 3))
print(b2.make_move(1, 3))
print(*b2.get_field(), sep="\n")
print(*b2.get_field(), sep="\n")