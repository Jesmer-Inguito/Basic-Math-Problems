import random
from tkinter import *

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
operations = ["+", "-", "*", "/"]
# Main Function
# Function for the answer ; var1 is the solving Entry (solving = Entry(app))
def answer(var1):
    if var1.get() == str(result()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.3, rely=0.2)
    else:
        wrong = Label(app, text="Wrong!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.3, rely=0.2)
# Function to try again
def try_again():
    # Clear the previous response
    for widget in app.winfo_children():
        if isinstance(widget, Label):
            widget.destroy
    
    # Clear the entry widget
    solving.delete(0, "end")

    num_1 = random.choice(num)
    num_2 = random.choice(num)
    operation = random.choice(operations)

    if operation == "-": # Bigger number - smaller number
        num_1, num_2 = max(num_1, num_2), min(num_1, num_2)


    question = Label(app, text=f"{num_1} {operation} {num_2}", font=("Courier", 14))
    question.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

    if operation == "/": # Avoid 0 / 0
        num_2 = random.choice([n for n in num if n != 0])
    elif operation == "-": # Avoid negative answers
        while num_1 - num_2 < 0:
            num_1 = random.choice(num)
            num_2 = random.choice(num)

    try_again.num1 = num_1
    try_again.num2 = num_2
    try_again.operation = operation
# (addition)
def result():
    if try_again.operation == "+":
        return try_again.num1 + try_again.num2
    elif try_again.operation == "-":
        return try_again.num1 - try_again.num2
    elif try_again.operation == "*":
        return try_again.num1 * try_again.num2
    elif try_again.operation == "/":
        return try_again.num1 / try_again.num2

# User Interface
app = Tk()
# Title
app.title("Math4Kids")

# Window
app.geometry("250x300")
app.resizable(False, False)

# Buttons and Textbox
start = Button(app, text="Press to Start", command=try_again)
start.place(relx=0.35, rely=0.2)

solving = Entry(app)
solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

submit = Button(app, text="Submit", command=lambda: answer(solving))
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

try_again = Button(app, text="Try Again", command=try_again)
try_again.place(relx=0.39, rely=0.9)

app.mainloop()
