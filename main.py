from tkinter import *
import pandas as pd
from random import *
import csv
BACKGROUND_COLOR = "#B1DDC6"

windows = Tk()
try:
    if len(pd.read_csv("data/progress.csv")) < 3:
        df = pd.read_csv("data/french_words.csv")
    else:
        df = pd.read_csv("data/progress.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
df = pd.DataFrame(df)
data = df.to_dict()
Frenchdict = [items for (word, items) in data.items() if word=="French"]
Englishdict = [items for (word, items) in data.items() if word=="English"]
Fr = [item for item in Frenchdict[0].values()]
En = [item for item in Englishdict[0].values()]
newfr = ""
neweng = ""
def back():
    global neweng
    canvas.itemconfig(tr, text=neweng, fill="white")
    canvas.itemconfig(before, image=PICC)
    canvas.itemconfig(betr, text="English", fill="white")

def back1():
    global neweng
    canvas.itemconfig(tr, text=neweng, fill="white")
    canvas.itemconfig(before, image=PICC)
    canvas.itemconfig(betr, text="English", fill="white")



def right():
    global neweng, newfr, flipt
    windows.after_cancel(flipt)
    newfr = choice(Fr)
    neweng = En[Fr.index(newfr)]
    canvas.itemconfig(tr, text=newfr, fill="black")
    canvas.itemconfig(betr, text="French", fill="black")
    canvas.itemconfig(before, image=PIC)
    Fr.pop(Fr.index(newfr))
    En.pop(En.index(neweng))
    flipt = windows.after(3000, func=back)
    Last = {}
    Last["French"] = Fr
    Last["English"] = En
    datad = pd.DataFrame.from_dict(Last)
    datad.to_csv("data/progress.csv", index=False)
def wrong():
    global neweng, newfr, flipt
    windows.after_cancel(flipt)
    newfr = choice(Fr)
    neweng = En[Fr.index(newfr)]
    canvas.itemconfig(tr, text=newfr, fill="black")
    canvas.itemconfig(betr, text="French", fill="black")
    canvas.itemconfig(before, image=PIC)
    flipt = windows.after(3000, func=back1)













flipt = windows.after(3000, func=back)
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
PIC = PhotoImage(file="images/card_front.png")
PICC = PhotoImage(file="images/card_back.png")
PIC1 = PhotoImage(file="images/right.png")
PIC2 = PhotoImage(file="images/wrong.png")
before = canvas.create_image(400, 263, image=PIC)
betr = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
tr = canvas.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
button_right = Button(image=PIC1, highlightthickness=0, command=right)
button_right.grid(column=0, row=1)
button_wrong = Button(image=PIC2, highlightthickness=0, command=wrong)
button_wrong.grid(column=1, row=1)
windows.mainloop()

