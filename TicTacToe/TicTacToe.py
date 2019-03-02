import tkinter
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self, start_turn, c):
        self.winner = '.'

    def add(self, x, y, c):
        if self.game_end:
            return
        if self.current_turn != c:
            return
        if self.board[(x * 3) + y] != '.':
            return
        
        self.board[(x * 3) + y] = c
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'

        self.winner = self.check_winner()
        if self.winner == 'O' or self.winner == 'X':
            messagebox.showinfo("게임 종료", self.winner + "가 이겼습니다.")
            self.game_end = True
        elif self.winner == 'd':
            messagebox.showinfo("게임 종료", "무승부입니다.")
            self.game_end = True

    def check_winner(self):
        for check in ["O", "X"]:
            for i in range(0, 3):
                if self.board[i * 3 + 0] == check and \
                    self.board[i * 3 + 1] == check and \
                    self.board[i * 3 + 2] == check:
                    return check
                if self.board[0 * 3 + i] == check and \
                    self.board[1 * 3 + i] == check and \
                    self.board[2 * 3 + i] == check:
                    return check
                if (self.board[0] == check and self.board[4] == check and self.board[8] == check) or \
                    (self.board[2] == check and self.board[4] == check and self.board[6] == check):
                    return check
        has_empty_cell = False
        for idx, val in enumerate(self.board):
            if val == '.':
                has_empty_cell = True
                break
            
        return '.' if has_empty_cell else 'd'

    def get_winner(self):
        return self.winner

    def get_current_turn(self):
        return self.current_turn

    def get(self, x, y):
        return self.board[(x * 3) + y]
    
    def show_board(self):
        for i in range(0, 9):
            print(self.board[i], end="")
            if (i + 1) % 3 == 0:
                print("")

    def draw_board(self):
        size = 100
        idx = 1
        x = 0
        y = 0
        for item in self.board:
            if item == '.':
                pass
            else:
                if item == 'O':
                    self.canvas.create_image(x+50, y+50, image=self.image['O'])
                elif item == 'X':
                    self.canvas.create_image(x + 50, y + 50, image=self.image['X'])
                x += size
                if idx % 3 == 0:
                    x = 0
                    y += size
            
            idx += 1
    def clear_board(self):
        self.canvas.delete('all')

class GameManager:
    def __init__(self):
        CANVAS_SIZE = 300
        self.TITLE_SIZE = int(CANVAS_SIZE / 3)
        
        self.root = tkinter.Tk()
        self.root.title("틱택토")
        self.root.geometry(str(CANVAS_SIZE) + 'x' +str(CANVAS_SIZE))
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, bg='white', width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()

        self.ttt = TicTacToe('O', self.canvas)
        self.canvas.bind('<Button-1>', self.click_handler)

    def click_handler(self, event):
        self.ttt.clear_board()

        self.turn = self.ttt.get_current_turn()
        self.ttt.add(math.floor(event.y / self.TITLE_SIZE), math.floor(event.x / self.TITLE_SIZE), self.turn)
        self.ttt.draw_board()

    def start(self):
        self.root.mainloop()

gm = GameManager()
gm.start()


    