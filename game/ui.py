from tkinter import *

root = Tk()
label = Label (width=40, text='Крестики-нолики')


def defaine_interface():
    buttons = [Button(width=20,height=5,bg='gray') for i in range(9)]
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