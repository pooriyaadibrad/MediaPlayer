import tkinter as tk
from tkinter import ttk

def select_first_row():
    tree.selection_set("item1")  # سلکت کردن اولین ردیف

root = tk.Tk()

tree = ttk.Treeview(root)
tree.pack()

tree.insert("", "0", "item1", text="مورد 1")
tree.insert("", "1", "item2", text="مورد 2")
tree.insert("", "end", "item3", text="مورد 3")

button = tk.Button(root, text="اولین ردیف", command=select_first_row)
button.pack()

root.mainloop()