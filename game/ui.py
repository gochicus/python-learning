from cgitb import text
from tkinter import *
import random

root = Tk()
label = Label (width=40, text='Крестики-нолики')
buttons = [Button(width=20,height=5,bg='gray',text='',command=lambda x=i:get_move(x)) for i in range(9)]

def get_move(x):
        buttons[x].config(text='X',bg='red')
        print(buttons[x].text)
  
def defaine_interface():
    label.grid(row=0,column=0,columnspan=3)
    row = 1
    column = 0
    for i in range(9):
        buttons[i].grid(row=row,column=column)
        column +=1
        if column==3:
            row+=1
            column =0
    root.mainloop()
    
defaine_interface()