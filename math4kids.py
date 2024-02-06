import random
import tkinter as tk

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Main Function
# Function for the answer ; var1 is the solving Entry (solving = Entry(app))
def answer(var1):
    if var1.get() == str(resultPLUS()):
        correct = tk.Label(app, text="Correct!", fg="green", font=("Courier", 14))
        correct.pack(padx=15, pady=15)
    else:
        wrong = tk.Label(app, text="Wrong!", fg="red", font=("Courier", 14))
        wrong.pack(padx=15, pady=15)
# Function to try again
def try_again():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)
    question = tk.Label(app, text=f"{try_again.num1update}+{try_again.num2update}", font=("Courier", 14))
    question.pack(padx=10, pady=10)
# Another function to try again
def resultPLUS():
    try_again

    return try_again.num1update + try_again.num2update

# User Interface
app = tk.Tk()
# Title
app.title("Math4Kids")

# Window
app.geometry("400x400")
app.resizable(True, True)

# Label
label = tk.Label(app, text="MATH4KIDS", font=("Times New Roman", 18))
label.pack(padx=20, pady=20)

# Buttons and Textbox
start = tk.Button(app, text="Press to Start", font=("Arial", 16), command=try_again)
start.pack(padx=10, pady=10)

solving = tk.Text(app, height=2, font=("Arial", 16))
solving.pack(padx=5, pady=5)

submit = tk.Button(app, text="Submit", font=("Arial", 16), command=lambda: answer(solving))
submit.pack(padx=10, pady=10)

try_again = tk.Button(app, text="Press to Try Again", font=("Arial", 16), command=try_again)
try_again.pack(padx=10, pady=10)

app.mainloop()
