import tkinter as tk
import tkinter.font as tkFont
from datetime import date
from time import strftime

def time():
    current_time = strftime("%I : %M : %S  %p")
    GLabel_846.config(text=current_time)
    GLabel_846.after(1000, time)

def day():
    today = date.today()
    current_date = today.strftime("%B %d, %Y")
    current_day = today.strftime("%A")
    GLabel_966.config(text=current_date+"\n"+current_day)
    GLabel_966.after(1000, day)


root = tk.Tk()
root.title("Digital Clock")
#setting window size
width=350
height=110
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

# day label size
GLabel_966=tk.Label(root)
GLabel_966["bg"] = "#f4d013"
GLabel_966["cursor"] = "watch"
GLabel_966["disabledforeground"] = "#775f5f"
ft = tkFont.Font(family='Times',size=15)
GLabel_966["font"] = ft
GLabel_966["fg"] = "#333333"
GLabel_966["justify"] = "center"
GLabel_966["relief"] = "flat"
GLabel_966.place(x=0,y=0,width=350,height=55)

# time label size
GLabel_846=tk.Label(root)
GLabel_846["activebackground"] = "#d72e2e"
GLabel_846["activeforeground"] = "#3b6b6c"
GLabel_846["anchor"] = "center"
GLabel_846["bg"] = "#1e1c1c"
GLabel_846["cursor"] = "watch"
ft = tkFont.Font(family='ds-digital',size=43)
GLabel_846["font"] = ft
GLabel_846["fg"] = "#be5b5b"
GLabel_846["justify"] = "center"
GLabel_846.place(x=0,y=55,width=350,height=55)



time()
day()
root.mainloop()

