"""
Create a window that will
ask the user to enter their
name. When they click on
a button it should display
the message “Hello” and
their name and change
the background colour
and font colour of the
message box.
"""


from tkinter import *

def Click():
	name = entry_box.get()
	message = str("Hola " + name)
	output_box["text"] = message

window = Tk()
window.geometry("500x200")
label = Label(text = "Enter your name:")
label.place(x=200, y=20)

entry_box = Entry(text = "")
entry_box.place(x=180, y=40, width=150, height=25)
entry_box["justify"] = "center"
entry_box.focus()

button1 = Button(text = "Press me", command = Click)
button1.place(x=180, y=70, width=150, height=25)

output_box = Message(text = "")
output_box.place(x=180, y=100, width=150, height=25)
output_box["bg"] = "white"
output_box["fg"] = "black"


window.mainloop()
