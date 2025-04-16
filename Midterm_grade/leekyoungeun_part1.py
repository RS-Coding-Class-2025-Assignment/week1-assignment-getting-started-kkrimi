import tkinter as tk
from tkinter import ttk

def convert(x):
    x = float(x)
    y = (x*9/5)+32
    return y


def cal():
    a = entry.get()
    result = convert(a)
    result_label.config(text=f"Result: {result}'F")
    
root = tk.Tk()
root.title("Celsius to Fahrenheit")
root.geometry("400x200")

Label = tk.Label(root, text="Enter Celsius")
Label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)

button = tk.Button(root, text="Convert", command=cal)
button.grid(row=1, column=0, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, pady=10)

root.mainloop()