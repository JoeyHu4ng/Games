import tkinter as tk


class Scoreboard:

    def __init__(self, scoreboard=None):
        self.scoreboard = {key: [] for key in ["Beginner", "Intermediate", "Expert"]}
        if scoreboard is not None:
            for key in scoreboard.keys():
                if key in self.scoreboard:
                    self.scoreboard[key] += scoreboard[key]
        self.mater = tk.Tk()
        self.mater.title("Scoreboard")

        self.menu = tk.Menu(self.mater)
        self.mater.config(menu=self.menu)

        self.submenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Level", menu=self.submenu)
        self.submenu.add_command(label="Beginner", command=lambda: self.__show_data("Beginner"))
        self.submenu.add_command(label="Intermediate", command=lambda: self.__show_data("Intermediate"))
        self.submenu.add_command(label="Expert", command=lambda: self.__show_data("Expert"))

        self.__show_data()

    def __show_data(self, level="Beginner"):
        scores = self.scoreboard[level]
        for i in range(10):
            rank = tk.Label(self.mater, height=1, width=4, text="No. %d" % (i + 1))
            rank.grid(row=i, column=0, columnspan=4, sticky=tk.W + tk.E + tk.N + tk.S)

            if i < len(scores):
                grade, name = scores[i]
            else:
                grade, name = "-" * 6, "-" * 20

            name_label = tk.Label(self.mater, height=1, width=20, text=name)
            name_label.grid(row=i, column=4, columnspan=20, sticky=tk.W + tk.E + tk.N + tk.S)
            grade_label = tk.Label(self.mater, height=1, width=6, text=grade)
            grade_label.grid(row=i, column=24, columnspan=6, sticky=tk.W + tk.E + tk.N + tk.S)


if __name__ == "__main__":
    scoreboard = Scoreboard({
        "Beginner": [(1, "joey"), (2, "Joey")],
        "Expert": [(11, "Joey")],
        "Intermediate": [(5, "Joey")],
        "Customized": [(0, "Joey")]
    })
    scoreboard.mater.mainloop()
