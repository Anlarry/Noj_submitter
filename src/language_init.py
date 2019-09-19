import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

def init_lan(var:tk.StringVar):
    inow_lan = 1  # c++
    try:
        with open(".\language.txt", "r") as F:
            inow_lan = int(F.readline())
            if inow_lan == 1:
                var.set("C++")
            else:
                var.set("G++")
    except IOError:
        tk.messagebox.showinfo(title="Hi", message="can not find language file")
