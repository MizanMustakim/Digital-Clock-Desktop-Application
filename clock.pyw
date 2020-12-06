from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Digital Clock")

def Time():
    current_time = strftime("%H : %M : %S  %p")
    label.config(text=current_time)
    label.after(1000, Time)

label = Label(window, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")
Time()

mainloop()