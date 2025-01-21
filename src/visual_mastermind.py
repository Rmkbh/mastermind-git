import random
import tkinter as tk
from tkinter import messagebox

def set_code():
    colours = ['b', 'y', 'r', 'g', 'o', 'p']
    code = []
    for i in range(4):
        code.append(random.choice(colours))
    return code

def mark_guess(guess, secret_code):
    code = secret_code.copy()
    guess_list = []
    for letter in guess:
        guess_list.append(letter)
    mark = []
    for i in range(0,len(guess_list)):
        if guess_list[i] == code[i]:
            mark.append('b')
            guess_list[i] = None
            code[i] = None
    for i in range(0,len(guess_list)):
        if guess_list[i] in code and guess_list[i] is not None:
            mark.append('w')
            code[code.index(guess_list[i])] = None
    return mark

def submit_guess():
    global secret_code, number_of_guesses

    guess = [peg.get() for peg in guess_vars]
    if any(colour not in colours for colour in guess):
        messagebox.showerror("Error", "Please select valid colours for all pegs")
        return 
    
    number_of_guesses +=1

    mark = mark_guess(guess, secret_code)
    display_guess(guess, mark)
    root.update_idletasks()

    if mark == ['b', 'b', 'b', 'b']:
        messagebox.showinfo("congratulations", f"You cracked the code in {number_of_guesses} guess(es)!")
        reset_game()

def display_guess(guess, mark):
    row_frame = tk.Frame(board_frame)
    row_frame.pack(pady=5, fill=tk.X)

    guess_frame = tk.Frame(row_frame)
    guess_frame.pack(side=tk.LEFT, padx=10)

    for colour in guess:
        peg = tk.Canvas(row_frame, width=30, height=30, bg=colours[colour])
        peg.pack(side=tk.LEFT, padx=5)

    mark_frame = tk.Frame(row_frame)
    mark_frame.pack(side=tk.RIGHT, padx=10)

    for m in mark:
        feedback_peg = tk.Canvas(mark_frame, width=15, height=15, bd=0, highlightthickness=0)
        if m == 'b':  
            feedback_peg.create_oval(2, 2, 13, 13, fill='black', outline='black')
        elif m == 'w':  
            feedback_peg.create_oval(2, 2, 13, 13, fill='white', outline='white')
        feedback_peg.pack(side=tk.LEFT, padx=2)


def reset_game():
    global secret_code, number_of_guesses

    secret_code = set_code()
    number_of_guesses = 0
    
    for widget in board_frame.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("Mastermind")

colours = {'b': 'blue', 'y': 'yellow', 'r': 'red', 'g': 'green', 'o': 'orange', 'p': 'pink'}
secret_code = set_code()
number_of_guesses = 0

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

guess_vars = []
for i in range(4):
    var = tk.StringVar(value="Select")
    dropdown = tk.OptionMenu(input_frame, var, *colours.keys())
    dropdown.pack(side=tk.LEFT, padx=5)
    guess_vars.append(var)

tk.Button(input_frame, text="Submit Guess", command=submit_guess).pack(side=tk.LEFT, padx=10)

board_frame = tk.Frame(root)
board_frame.pack(pady=10)

root.mainloop()



    





