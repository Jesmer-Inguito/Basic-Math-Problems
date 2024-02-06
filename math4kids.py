import random
import tkinter as tk

# User Interface
app = tk.Tk()

# Title
app.title("Math4Kids")

# Window
app.geometry("400x400")
app.resizable(False, False)

# Label
label = tk.Label(app, text="MATH4KIDS", font=("Time New Roman", 18))
label.pack(padx=20, pady=20)

# Buttons and Textbox
start = tk.Button(app, text="Press to Start", font=("Arial", 16))
start.pack(padx=10, pady=10)

text = tk.Text(app, height=2, font=("Arial", 16))
text.pack(padx=5, pady=5)

submit = tk.Button(app, text="Submit", font=("Arial", 16))
submit.pack(padx=10, pady=10)

try_again = tk.Button(app, text="Press to Try Again", font=("Arial", 16))
try_again.pack(padx=10, pady=10)

app.mainloop()
