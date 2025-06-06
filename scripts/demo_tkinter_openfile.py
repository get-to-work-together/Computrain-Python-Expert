import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename()

print(filename)
