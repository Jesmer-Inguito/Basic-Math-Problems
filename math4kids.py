import random
from tkinter import *

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Main Function
# Function for the answer ; var1 is the solving Entry (solving = Entry(app))
def answer(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.3, rely=0.2)
    else:
        wrong = Label(app, text="Wrong!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.3, rely=0.2)
# Function to try again
def try_again():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)
    question = Label(app, text=f"{try_again.num1update}+{try_again.num2update}", font=("Courier", 14))
    question.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)
# Another function to try again
def resultPLUS():
    try_again

    return try_again.num1update + try_again.num2update

# User Interface
app = Tk()
# Title
app.title("Math4Kids")

# Window
app.geometry("250x300")
app.resizable(False, False)

# Buttons and Textbox
start = Button(app, text="Start", command=try_again)
start.place(relx=0.45, rely=0.2)

solving = Entry(app)
solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

submit = Button(app, text="Submit", command=lambda: answer(solving))
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

try_again = Button(app, text="Try Again", command=try_again)
try_again.place(relx=0.39, rely=0.9)

app.mainloop()
