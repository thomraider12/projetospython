import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [[' ']*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('Arial', 30), width=3, height=1,
                                                command=lambda i=i, j=j: self.on_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                messagebox.showinfo("Parabéns!", f"Jogador {self.current_player} venceu!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Empate!", "O jogo terminou em empate.")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Check row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
            return True
        # Check column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
            return True
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ') or \
                (self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
                self.board[i][j] = ' '
        self.current_player = 'X'


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()