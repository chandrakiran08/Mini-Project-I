from tkinter import *
from tkinter import messagebox
from Solve import *
from Call import *
import pygame
import os

def ex():
    window.destroy()
    os._exit(0)
def play():
    messagebox.showinfo("showinfo", "Thanks for Playing \n Press 'TAB' for getting a Hint \n Press 'ESCAPE' to Auto Solve the Puzzle \n Press 'q' to Go back to Main Menu \n Press 'r' to Reset the Puzzle \n")
    create(0)
def solver():
    maze=[[0 for x in range(9)]for y in range(9)]
    createGUI(maze)

window = Tk()
window.title("Mini Project - I")
window.geometry('400x350')
window.config(background="black")
text=Label(window,text="SuDoKu",foreground="white",background="black",font=('Academy Engraved LET',100))
text.pack(pady=30)
b1 = Button(window,text='Play',command=play, font=("Courier New Bold", 20))
b1.pack(pady=5)
b2 = Button(window,text='Resolve',command = solver,font=("Courier New Bold", 20))
b2.pack(pady=5)
b3 = Button(window,text='Exit',command = ex,font=("Courier New Bold", 20))
b3.pack(pady=5)

window.mainloop()
