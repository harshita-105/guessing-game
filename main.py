import random
from tkinter import *
from tkinter import messagebox

no = random.randint(1,100)
attempt = 0

def sub():

    global attempt
    input = entr.get().strip()
    if not input.isdigit():
        messagebox.showwarning("Invalid Input", "Can only enter a number.")
        return

    guess = int(input)
    attempt += 1

    if guess < no:
        messagebox.showinfo("Result", f"Try higher. Attempts: {attempt}")
    elif guess > no:
        messagebox.showinfo("Result", f"Try lower. Attempts: {attempt}")
    else:
        messagebox.showinfo("Result", f"You've guessed the number {no} in {attempt} attempts.")

def clear():
    entr.delete(len(entr.get())-1,END)

window = Tk()
window.geometry("500x400")
window.title("Number Guessing Game")
icon = PhotoImage(file="img.png")
window.iconphoto(True,icon)
window.config(background= "black")

lbl = Label(window,
            text = "Number Guessing Game.",
            font= ("Pegasus", 20),
            fg ="black",
            relief="raised",
            bd=10 )
lbl.pack(pady=20)

inst = Label(window,
             text="Guess the random number!",
             font=("Pegasus", 18, "bold"),
             fg = "black")
inst.pack(pady=15)

entr = Entry(window,
             background="gray",
             font=("Pegasus", 18, "bold")
             )
entr.insert(0," ")
entr.pack(pady=15)

submit= Button(window,
               text="Ok",
               command= sub,
               background="gray",
               activebackground="gray",
               font=("Pegasus", 15, "bold"),
               foreground="black",
               activeforeground="black")
submit.pack(pady=15)

clr= Button(window,
               text="Clear",
               command= clear,
               background="gray",
               activebackground="gray",
               font=("Pegasus", 15, "bold"),
               foreground="black",
               activeforeground="black")
clr.pack(pady=15)

window.mainloop()












