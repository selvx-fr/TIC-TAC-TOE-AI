import tkinter as tk
from tkinter import simpledialog, messagebox

class TicTacToe:
    def __init__(self, root, player_symbol):
        self.root = root
        self.root.title("TIC-TAC-TOE - Human vs AI")
        self.player_symbol = player_symbol.upper()
        self.ai_symbol = 'O' if self.player_symbol == 'X' else 'X'

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]

        self.create_buttons()

        if self.player_symbol == 'O':
            self.root.after(500, self.ai_move)

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True)
        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text=' ', font=('Arial', 60), width=5, height=2,
                                command=lambda row=i, col=j: self.human_move(row, col))
                btn.grid(row=i, column=j, padx=10, pady=10)
                self.buttons[i][j] = btn

    def human_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.player_symbol
            self.buttons[row][col].config(text=self.player_symbol, state='disabled')
            if self.check_winner(self.player_symbol):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.root.after(500, self.ai_move)

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.ai_symbol
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = self.ai_symbol
            self.buttons[row][col].config(text=self.ai_symbol, state='disabled')

            if self.check_winner(self.ai_symbol):
                messagebox.showinfo("Game Over", "AI wins!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()

    def minimax(self, board, depth, is_max):
        if self.check_winner_static(board, self.ai_symbol):
            return 1
        elif self.check_winner_static(board, self.player_symbol):
            return -1
        elif self.is_draw_static(board):
            return 0

        if is_max:
            best = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = self.ai_symbol
                        best = max(best, self.minimax(board, depth + 1, False))
                        board[i][j] = ' '
            return best
        else:
            best = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = self.player_symbol
                        best = min(best, self.minimax(board, depth + 1, True))
                        board[i][j] = ' '
            return best

    def check_winner(self, player):
        return self.check_winner_static(self.board, player)

    def check_winner_static(self, board, player):
        for row in board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return self.is_draw_static(self.board)

    def is_draw_static(self, board):
        return all(cell != ' ' for row in board for cell in row)

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', state='normal')
        if self.player_symbol == 'O':
            self.root.after(500, self.ai_move)

def main():
    temp_root = tk.Tk()
    temp_root.withdraw()  

    player_symbol = ''
    while player_symbol.upper() not in ['X', 'O']:
        player_symbol = simpledialog.askstring("Choose Symbol", "Do you want to be X or O?", parent=temp_root)
        if player_symbol is None:
            exit()
    temp_root.destroy() 
    root = tk.Tk()
    game = TicTacToe(root, player_symbol)
    root.mainloop()

if __name__ == "__main__":
    main()