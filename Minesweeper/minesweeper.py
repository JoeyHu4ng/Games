import tkinter as tk
import random as random


class Minesweeper:
    def __init__(self, master):
        self.master = master
        self.grid = []
        self.board = []
        master.title("Minesweeper")

        OPTIONS = [
            "Beginner",
            "Intermediate",
            "Expert"
        ]

        global var
        var = tk.StringVar(master)
        var.set(OPTIONS[0])

        game = tk.OptionMenu(master, var, *OPTIONS)
        game.grid(row=0, column=0, columnspan=5, sticky=tk.W)

        button = tk.Button(master, text="OK", command=self.__set_size)
        button.grid(row=0, column=5, columnspan=2, sticky=tk.W)

        self.__set_size()

    def __set_size(self):
        OPTIONS = {
            "Beginner": [9, 9],
            "Intermediate": [16, 16],
            "Expert": [16, 30]
        }
        self.n, self.m = OPTIONS[var.get()][0], OPTIONS[var.get()][1]
        self.__set_grid()
        self.__set_mines()

    def __set_grid(self):
        for block in self.grid:
            block.grid_forget()
        self.board = []
        self.grid = []
        for i in range(self.n):
            for j in range(self.m):
                label = tk.Label(self.master, bg="gray", borderwidth=2, relief="groove", height=1, width=2)
                label.grid(row=i + 1, column=j, sticky=tk.W + tk.E + tk.N + tk.S)
                label.bind("<Button-1>", lambda e: e.widget.config(bg="darkgray"))
                self.grid.append(label)
                self.board.append(0)

    def __set_mines(self):
        OPTIONS = {
            "Beginner": 10,
            "Intermediate": 40,
            "Expert": 99
        }
        self.num_mines = OPTIONS[var.get()]
        mines = set()
        while len(mines) != self.num_mines:
            mines.add(random.randint(0, self.n * self.m - 1))
        for mine in mines:
            self.__set_mine(mine)
        self.__print_board()

    def __set_mine(self, mine):
        self.board[mine] = 9
        if mine - self.n > 0:
            self.board[mine - self.n] += 1
        if mine + self.m < self.n * self.m:
            self.board[mine + self.n] += 1
        if mine % self.n != 0:
            self.board[mine - 1] += 1
            if mine - self.n > 0:
                self.board[mine - self.n - 1] += 1
            if mine + self.m < self.n * self.m:
                self.board[mine + self.n - 1] += 1
        if mine % self.n != self.m - 1:
            self.board[mine + 1] += 1
            if mine - self.n > 0:
                self.board[mine - self.n + 1] += 1
            if mine + self.m < self.n * self.m:
                self.board[mine + self.n + 1] += 1

    def __print_board(self):
        for i in range(self.n * self.m):
            if i % self.n != self.m - 1:
                print("X" if self.board[i] > 8 else self.board[i], end="\t")
            else:
                print("X" if self.board[i] > 8 else self.board[i])


def main():
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()


if __name__ == '__main__':
    main()
