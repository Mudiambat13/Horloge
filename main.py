from tkinter import *
import datetime

windows = Tk()
windows.title("My Clock")
windows.geometry("300x200")

def time():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    clock.config(text=current_time)
    clock.after(1000, time)

clock = Label(windows, font=("Arial", 50), bg="black", fg="white")
clock.pack()
time()

windows.mainloop()