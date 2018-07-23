import tkinter as tk
import time as time

def knight(arr, x, y, res, d = 1):
    if arr[x][y] != -1:
        return False
    arr[x][y] = d
    res.append((x, y))
    if d == n*m:
        return True
    found = False
    for dx, dy in directions:
        newX = x + dx
        newY = y + dy
        if 0 <= newX < n and 0<= newY < m and knight(arr, newX, newY, res, d+1):
            return True
    if not found:
        arr[x][y] = -1
        res.pop()
        return False

def run(e):
    if len(res) == 0:
        root.quit()
    prev = None
    while len(res) != 0:
        i, j = res[0]
        L = labels[i*n+j]
        L.config(bg="darkred" if (i+j) % 2 == 0 else "red", text="%d" %arr[i][j], image=knight)
        if prev:
            prev.config(image='')
        prev = L
        res.pop(0)
        root.update()
        time.sleep(0.5)

def main():
    global n, m, directions, res, root, arr, labels, knight
    n = 7
    m = 7
    directions = [
        (1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)
    ]
    arr = [[-1 for i in range(m)] for j in range(n)]
    res = []
    knight(arr, 3, 3, res)
    print(res)

    root = tk.Tk()
    labels = []
    knight = tk.PhotoImage(file="knight.png")
    for i, row in enumerate(arr):
        for j, column in enumerate(row):
            L = tk.Label(root, bg="#769656" if (i+j) % 2 == 0 else "#eeeed2", width="10", height="5")
            L.grid(row=i, column=j, sticky=tk.W+tk.E+tk.N+tk.S)
            L.bind('<Button-1>', run)
            labels.append(L)
    root.mainloop()

if __name__ == "__main__" :
    main()
