from tkinter import *

die = {"🎲","⚀","⚁","⚂","⚃","⚄","⚅"}

App = Tk()

dice = Label(App, text=die[0], font=("Helvetica", "100")), foreground="white"
dice.grid(row=0, column=0, padx=1, pady=5)

def roll():
  from random import randint
  i = randint(1,6)
  msg = Label(App, text=die[i], font=("Helvetica", "100")), foreground="white"
  dice.grid(row=0, column=0, padx=1, pady=5)

rollB = Button(App, text="Roll", command=roll)
rollB.grid(row=1, column=0)

App.mainloop()