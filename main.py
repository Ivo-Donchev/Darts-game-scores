import tkinter

from darts import *

player1 = Player('player1')
player2 = Player('player2')
game = Game(player1, player2)

for i in range(1, 11):
    game.set_attempt(player1, i, i * 10)

for i in range(1, 11):
    game.set_attempt(player2, i, i * 20)

game.save()
width = "500"
height = "500"


# Code to add widgets will go here...
def submit(player1_entry, player2_entry):
    print(player1_entry)
    print(player2_entry)

top = tkinter.Tk()
top.geometry('{}x{}'.format(width, height))

submit_result = tkinter.Button(top,
                               width=20,
                               text="Try 1",
                               command=lambda: submit(player1_entry.get(), player2_entry.get()))


darts_label = tkinter.Label(top,
                            text="DARTS",
                            width=30)


player1_label = tkinter.Label(top, text=player1.name)
player1_entry = tkinter.Entry(top, bd=5)

player2_label = tkinter.Label(top, text=player2.name)
player2_entry = tkinter.Entry(top, bd=5)

submit_result.grid(row=3, column=1)

player1_label.grid(row=1, column=0)
player1_entry.grid(row=2, column=0)

player2_label.grid(row=1, column=2)
player2_entry.grid(row=2, column=2)

darts_label.grid(row=0, column=1)

top.mainloop()
