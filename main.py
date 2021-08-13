import tkinter as tk
from tkinter import messagebox, Toplevel, ttk, PhotoImage
from ttkbootstrap import Style

def move(event):
    window.gemoetry(f'+{0}+{1}'.format(event.x_root, event.y_root))


def addbillpressed():
    global window, screen, reason, amount
    if reason.get() != '' and amount.get() != '':
        messagebox.showinfo('DONE', 'Bill Succesfully Added!')
        screen.destroy()
    else:
        messagebox.showerror('ERROR', 'Please fill all details')

def addbill():
    global window, screen, reason, amount
    screen = Toplevel(window)
    screen.title('Add a Bill')
    screen.geometry('500x500')
    style = Style(screen)
    style.theme_use('cyborg')
    ttk.Label(screen, text='Payed For:').pack()
    reason = ttk.Entry(screen)
    reason.pack()
    ttk.Label(screen, text='').pack()
    ttk.Label(screen, text='Amount Payed:').pack()
    amount = ttk.Entry(screen)
    amount.pack()
    ttk.Label(screen, text='').pack()
    ttk.Button(screen, text='Add Bill', command=addbillpressed).pack()

def main():
    global window, splashscreen
    splashscreen.destroy()
    window = tk.Tk()
    window.geometry("800x600")
    style = Style(window)
    style.theme_use('cyborg')
    window.title("REVENUE TOOLS")
    ttk.Button(window, text='Add a Bill', command=addbill).pack()
    window.mainloop()

global splashscreen
splashscreen = tk.Tk()
splashscreen.geometry('300x250')
splashscreen.overrideredirect(1)
tk.Label(splashscreen, text='REVENUE TOOLS').pack()
tk.Label(splashscreen, text='').pack()
per = tk.Label(splashscreen, text='Loading...')
per.pack()
splashscreen.after(5000, main)

splashscreen.mainloop()
