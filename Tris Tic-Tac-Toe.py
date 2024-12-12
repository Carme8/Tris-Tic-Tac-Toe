import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tris TicTacToe")
        self.root.configure(bg='black')
        self.player = "X"
        self.board = [""] * 9
        self.score_x = 0
        self.score_o = 0

        self.buttons = []
        self.create_widgets()
        self.update_score()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("ARCADECLASSIC", 50), width=5, height=2,
                               command=lambda i=i: self.make_move(i), bg="black", fg="white", borderwidth=2, relief="solid")
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        self.score_label = tk.Label(self.root, text="", font=("ARCADECLASSIC", 18), bg='black', fg='white')
        self.score_label.grid(row=3, column=0, columnspan=3)

        
        self.reset_label = tk.Label(self.root, text="RESET", bg='black', fg='#34eb52', font=("ARCADECLASSIC", 25))
        self.reset_label.grid(row=4, column=0, columnspan=3, pady=(10, 20))
        self.reset_label.bind("<Button-1>", self.reset_game) 

    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.player
            color = "#34eb52" if self.player == "X" else "#000000"
            self.buttons[index].config(text=self.player, bg="black", fg=color)
            if self.check_winner():
                self.update_score()
                messagebox.showinfo("Victory!", f"Player {self.player} You Won!!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Tie!!", "It's a tie!")
                self.reset_board()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                if self.board[combo[0]] == "X":
                    self.score_x += 1
                else:
                    self.score_o += 1
                return True
        return False

    def update_score(self):
        self.score_label.config(text=f"Player X: {self.score_x}  Player O: {self.score_o}")

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", bg="black", fg="white") 
        self.player = "X"

    def reset_game(self, event=None):
        self.score_x = 0
        self.score_o = 0
        self.update_score()
        self.reset_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
