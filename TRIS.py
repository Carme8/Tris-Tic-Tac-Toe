import tkinter as tk
import tkinter.font as tkfont

class Tris2024:
    def __init__(self, master):
        self.master = master
        master.title("Tris")

        # FONT
        self.custom_font = tkfont.Font(family="ARCADECLASSIC", size=30)

        # LAYOUT GRIGLIA
        self.grid_buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text="", width=10, height=5, font=self.custom_font, 
                                   fg="magenta", command=lambda x=i, y=j: self.make_move(x, y))
                button.grid(row=i, column=j)
                row.append(button)
            self.grid_buttons.append(row)

        # GIOCATORI E PUNTEGGIO
        self.current_player = "X"
        self.score_x = 0
        self.score_o = 0
        self.status_label = tk.Label(master, text=f"Turno di: {self.current_player}", 
                                      font=tkfont.Font(family="ARCADECLASSIC", size=24), 
                                      fg="teal")
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Pulsanti per il reset e per uscire
        self.reset_button = tk.Button(master, text="RESET", font=self.custom_font, 
                                       fg="grey", command=self.reset_game)  
        self.reset_button.grid(row=4, column=0, padx=10, pady=10)
        self.quit_button = tk.Button(master, text="EXIT", font=self.custom_font, 
                                      fg="grey", command=master.quit)
        self.quit_button.grid(row=4, column=2, padx=10, pady=10)

    def make_move(self, row, col):
        if self.grid_buttons[row][col]["text"] == "":
            self.grid_buttons[row][col]["text"] = self.current_player
            
            if self.current_player == "X":
                self.grid_buttons[row][col]["fg"] = "teal"
            else:
                self.grid_buttons[row][col]["fg"] = "grey" 
            
            if self.check_win(self.current_player):
                if self.current_player == "X":
                    self.score_x += 1
                else:
                    self.score_o += 1
                self.status_label["text"] = f"{self.current_player} ha vinto! Punteggio X: {self.score_x}, O: {self.score_o}"
                self.disable_board()
            elif self.check_tie():
                self.status_label["text"] = "Pareggio!"
                self.disable_board()
            else:
                self.switch_player()

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        self.status_label["text"] = f"Turno di: {self.current_player}"

    def check_win(self, player):
        for i in range(3):
            if self.grid_buttons[i][0]["text"] == self.grid_buttons[i][1]["text"] == self.grid_buttons[i][2]["text"] == player:
                return True
        for i in range(3):
            if self.grid_buttons[0][i]["text"] == self.grid_buttons[1][i]["text"] == self.grid_buttons[2][i]["text"] == player:
                return True
        if self.grid_buttons[0][0]["text"] == self.grid_buttons[1][1]["text"] == self.grid_buttons[2][2]["text"] == player:
            return True
        if self.grid_buttons[0][2]["text"] == self.grid_buttons[1][1]["text"] == self.grid_buttons[2][0]["text"] == player:
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.grid_buttons[i][j]["text"] == "":
                    return False
        return True

    def disable_board(self):
        for i in range(3):
            for j in range(3):
                self.grid_buttons[i][j]["state"] = "disabled"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.grid_buttons[i][j]["text"] = ""
                self.grid_buttons[i][j]["state"] = "normal"
        self.current_player = "X"
        self.status_label["text"] = f"Turno di: {self.current_player}"

root = tk.Tk()
game = Tris2024(root)
root.mainloop()