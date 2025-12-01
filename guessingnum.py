import tkinter as tk
from tkinter import messagebox
import random
import sys

lower_limit = 1
upper_limit = 10
secret_number = random.randint(lower_limit, upper_limit)

def check_guess():
    user_guess = int(guess_entry.get())
    if user_guess == secret_number:
        messagebox.showinfo("Congratulations", "Congratulations! You guessed it!")
    elif user_guess < secret_number:
        result_label.config(text="Try a higher number.")
    else:
        result_label.config(text="Try a lower number.")

def exit_game():
    root.destroy()

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x200")
root.configure(bg="pink1")

instructions_label = tk.Label(root, text=f"Guess a number between {lower_limit} and {upper_limit}:", bg="pink1")
instructions_label.grid(row=0, column=0, columnspan=2)

guess_entry = tk.Entry(root)
guess_entry.grid(row=1, column=0, columnspan=2)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.grid(row=2, column=0)

exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.grid(row=2, column=1)

result_label = tk.Label(root, text="", bg="pink1")
result_label.grid(row=3, column=0, columnspan=2)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
