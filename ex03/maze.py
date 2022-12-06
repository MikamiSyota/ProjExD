import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc1():
    global c1x, c1y, m1x, m1y
    if key == "Up": m1y -= 1
    if key == "Down": m1y += 1
    if key == "Left": m1x -= 1
    if key == "Right": m1x += 1
    if key == "s":
        m1x = 1
        m1y = 1
    if maze_lst[m1x][m1y] == 1: #移動先が壁だったら
        if key == "Up": m1y += 1
        if key == "Down": m1y -= 1
        if key == "Left": m1x += 1
        if key == "Right": m1x -= 1
    c1x = m1x*100+50
    c1y = m1y*100+50
    canvas.coords("kokaton1", c1x, c1y)
    root.after(100, main_proc1)

def main_proc2():
    global c2x, c2y, m2x, m2y
    if key == "i": m2y -= 1
    if key == "m": m2y += 1
    if key == "j": m2x -= 1
    if key == "l": m2x += 1
    if key == "g":
        m2x = 13
        m2y = 7
    if maze_lst[m2x][m2y] == 1: #移動先が壁だったら
        if key == "i": m2y += 1
        if key == "m": m2y -= 1
        if key == "j": m2x += 1
        if key == "l": m2x -= 1
    c2x = m2x*100+50
    c2y = m2y*100+50
    canvas.coords("kokaton2", c2x, c2y)
    root.after(100, main_proc2)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)

    kokaton1 = tk.PhotoImage(file="../fig/6.png")
    kokaton2 = tk.PhotoImage(file="../fig/2.png")

    m1x = 1
    m1y = 1
    m2x = 13
    m2y = 7
    c1x = m1x*100+50
    c1y = m1y*100+50
    c2x = m2x*100+50
    c2y = m2y*100+50
    
    canvas.create_image(c1x, c1y, image=kokaton1, tag="kokaton1")
    canvas.create_image(c2x, c2y, image=kokaton2, tag="kokaton2")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc1()
    main_proc2()
    root.mainloop()