import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    i = btn["text"]
    # tkm.showinfo(i, f"[{i}]ボタンがクリックされました")
    if i == "=":
        None
    else:
        entry.insert(tk.END, i)

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

entry = tk.Entry(root, justify="right", width=10, font=("", 40))
entry.grid(row=0, column=0, columnspan=3)


r = 1
c = 0
for i in range(9, -1, -1):
    button = tk.Button(root, text=f"{i}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    button.grid()
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0

operators = ["+", "="]
for ad_pl in operators:
    button = tk.Button(root, text=f"{ad_pl}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()