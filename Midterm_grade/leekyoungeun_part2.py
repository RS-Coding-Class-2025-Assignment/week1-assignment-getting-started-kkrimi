import tkinter as tk
from tkinter import ttk
import time
import threading


root = tk.Tk()
root.title("part2")

progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=20)

Label = tk.Label(root, text="Ready")
Label.pack()

def start():
    for i in range(101):
        Label.config(text=f"{i}%")
        root.update()
        time.sleep(1.2)
    
def stop():
    progress["value"]=0
    label.config(text="0%")

start_button = tk.Button(root, text="Start", command=start)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack()

root.mainloop()


















# stop_thread = False

# root = tk.Tk()
# root.title("Example 4:Progress Bar+Thread")

# progress = ttk.Progressbar(root, orient="vertical", length=200, mode="determinate")
# progress.pack(pady=20)

# label = tk.Label(root, text="Ready")
# label.pack(pady=20)

# # progress bar
# def run_in_thread():
#     for i in range(101):
#         global stop_thread
#         if stop_thread:
#             break
#         label.config(text=f"{i}%")
#         progress.step(1)
#         root.update()
#         time.sleep(0.2)

# # start
# def start_thread():
#     global stop_thread
#     stop_thread = False
#     progress["value"]=0
#     label.config(text="0%")
#     t=threading.Thread(target=run_in_thread)
#     t.start()
#     start_button.config(state=tk.DISABLED)
#     stop_button.config(state=tk.NORMAL)

# # stop
# def stop():
#     global stop_thread
#     stop_thread = True
#     progress["value"]=0
#     label.config(text="0%")
#     start_button.config(state=tk.NORMAL)
#     stop_button.config(state=tk.DISABLED)

# start_button = tk.Button(root, text="Start", command=start_thread)
# start_button.pack(pady=10)

# stop_button = tk.Button(root, text="Stop", command=stop)
# stop_button.pack(pady=10)
# stop_button.config(state=tk.DISABLED)
# root.mainloop()