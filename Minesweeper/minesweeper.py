import tkinter as tk
import random as random


class Minesweeper:
    def __init__(self, master, size=8):
        self.size = size
        self.master = master
        self.grid = []
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
        game.grid(row=0, column=0)

        button = tk.Button(master, text="OK", command=self.__change_size)
        button.grid(row=0, column=1)

        self.__set_grid()

    def __change_size(self):
        OPTIONS = {
            "Beginner": 8,
            "Intermediate": 16,
            "Expert": 24
        }
        self.size = OPTIONS[var.get()]
        self.__set_grid()

    def __set_grid(self):
        for block in self.grid:
            block.grid_forget()
        for i in range(self.size):
            for j in range(self.size):
                label = tk.Label(self.master, bg="gray", borderwidth=2, relief="groove", height=2, width=5)
                label.grid(row=i+1, column=j, sticky=tk.W+tk.E+tk.N+tk.S)
                label.bind("<Button-1>", lambda e: e.widget.config(bg="darkgray"))
                self.grid.append(label)


def main():
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()


if __name__ == '__main__':
    main()
