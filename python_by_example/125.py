"""
Dices
Write a program that
can be used instead
of rolling a six-sided
die in a board game.
When the user clicks
a button it should
display a random
whole number
between 1 to 6
(inclusive).
"""

from tkinter import *
import random

def Click():
    num = random.randint(1,6)
    answer["text"] = num


window = Tk()
window.geometry("200x180")

button1 = Button(text = "Roll dice", command = Click)
button1.place(x=40, y=30, width=120, height=25)

answer = Message(text = "")
answer.place(x=40, y=80, width=120, height=25)
answer["bg"] = "white"
answer["fg"] = "black"

window.mainloop()
