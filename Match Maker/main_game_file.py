import random
import time 
from tkinter import Tk,Button,DISABLED


def show_symbol(v,g):
    global first
    global previousx,previousy
    buttons[v,g]['text'] = button_symbol[v,g]
    buttons[v,g].update_idletasks()

    if first:
        previousx = v
        previousy = g
        first = False
    elif previousx!= v or previousy!=g:
        if buttons[previousx,previousy]['text'] != buttons[v,g]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[v,g]['text'] = ' '
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[v,g]['command'] = DISABLED
        first = True


win =Tk()
win.title("Match Maker")
win.resizable(width=False,height=False)
first = True
previousx = 0
previousy = 0

buttons ={}
button_symbol = {}
symbols =[u'\u2702',u'\u2705',u'\u2708',u'\u270A',u'\u270B',u'\u270C',u'\u270F',
        u'\u2712',u'\u2714',u'\u2716',u'\u2728',
        u'\u2702',u'\u2705',u'\u2708',u'\u270A',u'\u270B',u'\u270C',u'\u270F',
        u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbols)

for v in range(6):
    for g in range(4):
        button = Button(command=show_symbol(v,g), width=6,height=6)
        button.grid(column=v,row=g)
        buttons[v,g] = button
        button_symbol[v,g] = symbols.pop()

win.mainloop()