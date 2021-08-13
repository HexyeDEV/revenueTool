import tkinter as tk
from tkinter import messagebox, Toplevel, ttk, PhotoImage
from ttkbootstrap import Style
import time

progress = {}

def move(event):
    window.gemoetry(f'+{0}+{1}'.format(event.x_root, event.y_root))

def close():
    global window
    window.destroy()

def main():
    global window, splashscreen
    splashscreen.destroy()
    window = tk.Tk()
    window.geometry("800x600")
    style = Style(window)
    style.theme_use('cyborg')
    window.title("REVENUE TOOLS")
    window.mainloop()

global splashscreen
splashscreen = tk.Tk()
splashscreen.geometry('300x250')
splashscreen.overrideredirect(1)
tk.Label(splashscreen, text='REVENUE MANAGER').pack()
tk.Label(splashscreen, text='').pack()
per = tk.Label(splashscreen, text='Loading...')
per.pack()
splashscreen.after(5000, main)

splashscreen.mainloop()
