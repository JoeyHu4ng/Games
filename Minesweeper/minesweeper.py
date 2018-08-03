import tkinter as tk
import random as random
import time as time
import math as math
from Minesweeper.scoreboard import Scoreboard
from tkinter import simpledialog
from PIL import Image, ImageTk


class Minesweeper:
    size_ops = {
        "Beginner": (9, 9),
        "Intermediate": (16, 16),
        "Expert": (16, 30)
    }

    mines_ops = {
        "Beginner": 10,
        "Intermediate": 40,
        "Expert": 99
    }

    colors_ops = {
        1: "blue",
        2: "green",
        3: "red",
        4: "purple",
        5: "maroon",
        6: "turquoise",
        7: "black",
        8: "gray"
    }

    def __init__(self, master, title="Minesweeper"):
        self.master = master
        self.master.title(title)

        self.grid = []
        self.board = []
        self.status = []
        self.flags = []
        self.__set_size()
        self.__load_scoreboard()
        self.master.resizable(False, False)

        self.flag = ImageTk.PhotoImage(Image.open("images/flag.png"))
        self.mine = ImageTk.PhotoImage(Image.open("images/mine.png"))
        self.dead_mine = ImageTk.PhotoImage(Image.open("images/dead_mine.png"))
        self.wrong_mine = ImageTk.PhotoImage(Image.open("images/wrong_mine.png"))
        self.smile = ImageTk.PhotoImage(Image.open("images/smile.png"))
        self.over = ImageTk.PhotoImage(Image.open("images/over.png"))
        self.cool = ImageTk.PhotoImage(Image.open("images/cool.png"))

        self.__set_menu_bar()
        self.__set_counter()
        self.__set_grid()

    def __set_menu_bar(self):
        """ Set the menu toolbar for change size and score board. """
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.submenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Game", menu=self.submenu)
        self.submenu.add_command(label="Beginner", command=lambda: self.__update_board("Beginner"))
        self.submenu.add_command(label="Intermediate", command=lambda: self.__update_board("Intermediate"))
        self.submenu.add_command(label="Expert", command=lambda: self.__update_board("Expert"))
        self.submenu.add_command(label="Scoreboard", command=self.show_scoreboard)

    def __set_counter(self):
        """ Set up mines counter, smile face, and timer."""
        # set up mines counter
        self.mines_left_label = tk.Label()
        self.mines_left_label.grid(row=0, columnspan=self.m, sticky=tk.W + tk.N + tk.S)
        self.__update_mines_left()

        # set up smile face
        self.smile_face = tk.Label(image=self.smile)
        self.smile_face.grid(row=0, columnspan=self.m, sticky=tk.N + tk.S)
        self.smile_face.bind("<Button-1>", lambda e: self.__update_board(self.level))

        # set up timer
        self.timer = tk.Label(text=0)
        self.timer.grid(row=0, columnspan=self.m, sticky=tk.E + tk.N + tk.S)

    def __set_size(self, level="Beginner"):
        self.level = level
        self.n, self.m = self.size_ops[self.level]
        self.total_mines = self.mines_ops[self.level]
        self.mines_left = self.total_mines
        self.finished = False
        self.mine_generated = False
        self.start_time = None
        self.win = False

    def __set_grid(self):
        """ clean the old board and create new board. """
        self.__clean_board()
        for i in range(self.n):
            for j in range(self.m):
                label = tk.Label(self.master, bg="gray", borderwidth=2, relief="groove", height=1, width=2)
                label.grid(row=i + 1, column=j, sticky=tk.W + tk.E + tk.N + tk.S)
                label.bind("<Button-1>", self.__left_click)
                label.bind("<Button-3>", self.__right_click)
                label.bind("<Double-Button-1>", self.__double_click)
                self.grid.append(label)
                self.board.append(0)
                self.status.append(False)

    def __generate_mines(self, ignore):
        self.mines = random.sample([x for x in range(self.n * self.m) if x != ignore], self.total_mines)
        self.flags = []
        for mine in self.mines:
            self.__set_mine(mine)
        self.mine_generated = True

    def __set_mine(self, mine):
        self.board[mine] = 9
        for block in self.__find_neighbor(mine):
            self.board[block] += 1

    def __update_board(self, level):
        self.__set_size(level)
        self.mines_left_label.grid_forget()
        self.smile_face.grid_forget()
        self.timer.grid_forget()
        self.__set_counter()
        self.__set_grid()

    def __update_mines_left(self):
        self.mines_left_label.config(text=max(self.mines_left, 0))

    def __update_timer(self):
        if self.start_time is not None and not self.finished:
            self.time = time.time() - self.start_time
            self.timer.config(text=math.floor(self.time))
            self.master.after(1000, self.__update_timer)

    def __left_click(self, e, block=None):
        if self.finished:
            return

        if self.start_time is None:
            self.start_time = time.time()
            self.__update_timer()

        block = block if block is not None else self.grid.index(e.widget)

        if not self.mine_generated:
            self.__generate_mines(block)

        if self.status[block] == 'f':
            return
        # put all kinds of mines and game over
        elif self.board[block] > 8:
            self.finished = True
            self.grid[block].config(image=self.dead_mine, anchor=tk.CENTER)
            self.mines.remove(block)
            for mine in self.mines:
                if mine in self.flags:
                    self.grid[mine].config(image=self.flag, anchor=tk.CENTER)
                    self.flags.remove(mine)
                else:
                    self.grid[mine].config(image=self.mine, anchor=tk.CENTER)
            for mine in self.flags:
                self.grid[mine].config(image=self.wrong_mine, anchor=tk.CENTER)
        elif not self.status[block]:
            self.__open_area(block)
            if self.finished:
                for mine in self.mines:
                    self.grid[mine].config(image=self.flag, anchor=tk.CENTER)
                self.num_mines_left = 0
                self.__update_mines_left()

        if self.finished:
            self.__update_scoreboard()

    def __open_area(self, block):
        if block < 0 or block >= self.n * self.m or self.status[block]:
            return
        elif self.board[block] > 0:
            self.grid[block].config(text=self.board[block],
                                    bg="darkgray", fg=self.colors_ops[self.board[block]])
            self.status[block] = True
            if self.status.count(True) == self.n * self.m - self.total_mines:
                self.finished = True
                self.win = True
        else:
            self.grid[block].config(bg="darkgray")
            self.status[block] = True
            for block in self.__find_neighbor(block):
                self.__open_area(block)

    def __right_click(self, e):
        if self.finished:
            return

        if self.start_time is None:
            self.start_time = time.time()
            self.__update_timer()

        block = self.grid.index(e.widget)

        if self.status[block] == 'f':
            e.widget.config(image='')
            self.flags.remove(block)
            self.status[block] = False
            self.mines_left += 1
        elif not self.status[block]:
            e.widget.config(image=self.flag)
            self.flags.append(block)
            self.status[block] = 'f'
            self.mines_left -= 1
        self.__update_mines_left()

    def __double_click(self, e):
        block = self.grid.index(e.widget)
        if self.status[block] is True and self.board[block] > 0:
            neighbor = {key: self.status[key] for key in self.__find_neighbor(block)}
            if list(neighbor.values()).count('f') == self.board[block]:
                for key in neighbor.keys():
                    if not neighbor[key]:
                        self.__left_click(e, key)

    def __find_neighbor(self, block):
        neighbor = [x for x in self.__check_horizontal(block)]
        if block % self.m != 0:
            neighbor.append(block - 1)
            neighbor += self.__check_horizontal(block - 1)
        if block % self.m != self.m - 1:
            neighbor.append(block + 1)
            neighbor += self.__check_horizontal(block + 1)
        return neighbor

    def __check_horizontal(self, block):
        res = []
        if block - self.m >= 0:
            res.append(block - self.m)
        if block + self.m < self.n * self.m:
            res.append(block + self.m)
        return res

    def __clean_board(self):
        for button in self.grid:
            button.grid_forget()
        self.grid = []
        self.board = []
        self.status = []

    def __update_scoreboard(self):
        if self.win:
            self.smile_face.config(image=self.cool)
            if len(self.scoreboard[self.level]) < 10 or self.time < self.scoreboard[self.level][-1][0]:
                name = simpledialog.askstring("Congratulations", "Please enter your name:")
                name = "Anonymous" if name is None or len(name) == 0 else name
                self.scoreboard[self.level].append((math.floor(self.time), name))
                self.scoreboard[self.level].sort()
                if len(self.scoreboard[self.level]) >= 10:
                    self.scoreboard[self.level].pop()
                self.__write_scoreboard()
        else:
            self.smile_face.config(image=self.over)

    def __load_scoreboard(self):
        self.scoreboard = {key: [] for key in self.size_ops.keys()}
        try:
            scoreboard_file = open("scoreboard", "r")
            lines = scoreboard_file.readlines()
            for line in lines:
                line = line.strip().split()
                self.scoreboard[line[0]].append((int(line[-1]), " ".join(line[1:-1])))
            for level in self.scoreboard.keys():
                self.scoreboard[level].sort()
        except FileNotFoundError:
            return

    def __write_scoreboard(self):
        scoreboard_file = open("scoreboard", "w+")
        for level in self.scoreboard.keys():
            count = 0
            for grade, name in self.scoreboard[level]:
                scoreboard_file.write(level + " ")
                scoreboard_file.write(name + " " + str(grade) + "\n")
                count += 1
        scoreboard_file.close()

    def __print_whole_board(self):
        """ Print whole board status. """
        print("#" * self.m + " " + self.level + " " + "#" * self.m)
        for i in range(self.n * self.m):
            if i % self.m != self.m - 1:
                print("X" if self.board[i] > 8 else self.board[i], end="\t")
            else:
                print("X" if self.board[i] > 8 else self.board[i])

    def show_scoreboard(self):
        scoreboard_label = Scoreboard(self.scoreboard)
        scoreboard_label.mater.mainloop()


def main():
    game = Minesweeper(tk.Tk())
    game.master.mainloop()


if __name__ == '__main__':
    main()
