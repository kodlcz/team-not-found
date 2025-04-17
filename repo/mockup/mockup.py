import tkinter as tk
from tkinter import messagebox
import calc_lib  # ← tvá knihovna s funkcemi

def insert_char(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def calculate(): #potřebuje rework, nepoužívá naši knihovnu
    try:
        expr = entry.get()
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def call_factorial():
    try:
        n = int(entry.get())
        result = calc_lib.factorial(n)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def call_power():
    try:
        parts = entry.get().split("^")
        base = int(parts[0])
        exp = int(parts[1])
        result = calc_lib.power(base, exp)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def call_root():
    try:
        parts = entry.get().split("√")
        degree = int(parts[0])
        number = float(parts[1])
        result = calc_lib.root(number, degree)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def call_fibonacci():
    try:
        n = int(entry.get())
        result = calc_lib.fibonacci(n)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def show_help():
    messagebox.showinfo("Nápověda", """
Základní operace: +, -, *, /
Mocnina: zadej jako: základ^exponent a stiskni ^= 
Obecná odmocnina: zadej jako: stupeň√číslo a stiskni √=
Faktoriál: zadej celé číslo a stiskni !
Fibonacci: zadej n a stiskni Fib
""")

root = tk.Tk()
root.title("Kalkulačka")

entry = tk.Entry(root, width=25, font=("Arial", 16), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ("7", lambda: insert_char("7")),
    ("8", lambda: insert_char("8")),
    ("9", lambda: insert_char("9")),
    ("/", lambda: insert_char("/")),
    ("4", lambda: insert_char("4")),
    ("5", lambda: insert_char("5")),
    ("6", lambda: insert_char("6")),
    ("*", lambda: insert_char("*")),
    ("1", lambda: insert_char("1")),
    ("2", lambda: insert_char("2")),
    ("3", lambda: insert_char("3")),
    ("-", lambda: insert_char("-")),
    ("0", lambda: insert_char("0")),
    (".", lambda: insert_char(".")),
    ("+", lambda: insert_char("+")),
    ("=", calculate),
    ("C", clear),
    ("⌫", backspace),
    ("!", call_factorial),
    ("^", lambda: insert_char("^")),
    ("√", lambda: insert_char("√")),
    ("^=", call_power),
    ("√=", call_root),
    ("Fib", call_fibonacci),
    ("?", show_help)
]

row = 1
col = 0
for (text, command) in buttons:
    btn = tk.Button(root, text=text, width=5, height=2, command=command)
    btn.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Klávesnice
def key_handler(event):
    if event.char in "0123456789+-*/.":
        insert_char(event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()

root.bind("<Key>", key_handler)

root.mainloop()
