import tkinter as tk
import random as random
import time as time
import math as math


class Minesweeper:
    def __init__(self, master):
        self.master = master
        self.grid = []
        self.board = []
        self.status = []
        self.finished = False
        self.win = False
        self.start_time = None
        self.flag = tk.PhotoImage(file="flag.png").subsample(3)
        self.mine = tk.PhotoImage(file="mine.png").subsample(8)
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
        self.__start_game()
        self.__set_timer()

    def __start_game(self):
        self.finished = False
        self.win = False
        self.start_time = None

    def __set_grid(self):
        for block in self.grid:
            block.grid_forget()
        self.board, self.grid, self.status = [], [], []
        for i in range(self.n):
            for j in range(self.m):
                label = tk.Label(self.master, bg="gray", borderwidth=2, relief="groove", height=1, width=2)
                label.grid(row=i + 2, column=j, sticky=tk.W + tk.E + tk.N + tk.S)
                label.bind("<Button-1>", self.__left_click)
                label.bind("<Button-3>", self.__right_click)
                self.grid.append(label)
                self.board.append(0)
                self.status.append(False)

    def __left_click(self, e):
        if self.finished:
            return

        if self.start_time is None:
            self.start_time = time.time()
            self.__update_clock()

        block = self.grid.index(e.widget)
        if self.status[block] == 'f':
            return
        elif self.board[block] > 8:
            self.finished = True
            for mine in self.mines:
                self.grid[mine].config(image=self.mine, anchor=tk.CENTER)
        elif not self.status[block]:
            self.__open_area(block)
            if self.finished:
                for mine in self.mines:
                    self.grid[mine].config(image=self.flag, anchor=tk.CENTER)
                self.num_mines_left = 0
                self.__update_num_mines_left()

    def __open_area(self, block):
        if block < 0 or block >= self.n * self.m or self.status[block]:
            return
        elif self.board[block] > 0:
            self.grid[block].config(text=self.board[block], bg="darkgray")
            self.status[block] = True
            if self.status.count(True) == self.n * self.m - self.num_mines:
                self.finished = True
                self.win = True
        else:
            self.grid[block].config(bg="darkgray")
            self.status[block] = True
            self.__open_horizontal(block)
            if block % self.m != 0:
                self.__open_area(block - 1)
                self.__open_horizontal(block - 1)
            if block % self.m != self.m - 1:
                self.__open_area(block + 1)
                self.__open_horizontal(block + 1)

    def __open_horizontal(self, block):
        self.__open_area(block - self.m)
        self.__open_area(block + self.m)

    def __right_click(self, e):
        if self.finished:
            return

        if self.start_time is None:
            self.start_time = time.time()
            self.__update_clock()

        block = self.grid.index(e.widget)
        if self.status[block] == 'f':
            e.widget.config(image="")
            self.status[block] = False
            self.num_mines_left += 1
            self.__update_num_mines_left()
        elif not self.status[block]:
            e.widget.config(image=self.flag)
            self.status[block] = 'f'
            self.num_mines_left -= 1
            self.__update_num_mines_left()

    def __set_mines(self):
        OPTIONS = {
            "Beginner": 10,
            "Intermediate": 40,
            "Expert": 99
        }
        self.num_mines = OPTIONS[var.get()]

        self.num_mines_left = self.num_mines
        self.num_mines_left_label = tk.Label()
        self.num_mines_left_label.grid(row=1, columnspan=self.m, sticky=tk.W)
        self.__update_num_mines_left()

        self.mines = random.sample(range(self.n * self.m), self.num_mines)
        for mine in self.mines:
            self.__set_mine(mine)
        self.__print_board()

    def __set_mine(self, mine):
        self.board[mine] = 9
        self.__check_horizontal(mine)
        if mine % self.m != 0:
            self.board[mine - 1] += 1
            self.__check_horizontal(mine - 1)
        if mine % self.m != self.m - 1:
            self.board[mine + 1] += 1
            self.__check_horizontal(mine + 1)

    def __check_horizontal(self, mine):
        if mine - self.m >= 0:
            self.board[mine - self.m] += 1
        if mine + self.m < self.n * self.m:
            self.board[mine + self.m] += 1

    def __set_timer(self):
        self.timer = tk.Label(text="0")
        self.timer.grid(row=1, columnspan=self.m, sticky=tk.E)

    def __update_clock(self):
        if self.start_time is not None and not self.finished:
            now = time.time() - self.start_time
            self.timer.config(text=math.floor(now))
            self.master.after(1000, self.__update_clock)

    def __update_num_mines_left(self):
        self.num_mines_left_label.config(text=max(self.num_mines_left, 0))

    def __print_board(self):
        print("#" * self.m + " board " + "#" * self.m)
        for i in range(self.n * self.m):
            if i % self.m != self.m - 1:
                print("X" if self.board[i] > 8 else self.board[i], end="\t")
            else:
                print("X" if self.board[i] > 8 else self.board[i])


def main():
    game = Minesweeper(tk.Tk())
    game.master.mainloop()


if __name__ == '__main__':
    main()
