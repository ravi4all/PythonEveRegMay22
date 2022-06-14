from asyncio import events
from cgitb import text
from tkinter import *

# initialize your window
window = Tk()
window.geometry('350x400')
window.title("My First GUI...")

textBox = Entry(window, width=25,font=(14), justify="right")
textBox.grid(row=0, columnspan=4, padx=10,pady=10,ipady=10, ipadx=4)

buttons = [
    ['c','<-','%','='],
    ['7','8','9','+'],
    ['4','5','6','-'],
    ['1','2','3','/'],
    ['.','0','e','*'],
]

def calculate(btn_obj):
    # print(btn_obj.widget.cget('text'))
    expression = btn_obj.widget.cget('text')
    if expression == "=":
        value = textBox.get()
        result = eval(value)
        textBox.delete(0, len(value))
        textBox.insert(0, result)
    else:
        value = textBox.get()
        textBox.insert(len(value),expression)

buttons_dict = {}
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        currentBtn = 'btn_{}'.format(buttons[i][j])
        btn = Button(window, text=buttons[i][j], width=5, font=(15),
         bg='red', fg='white')
        buttons_dict[currentBtn] = btn
        buttons_dict[currentBtn].grid(row=i+1, column=j, padx=5, pady=5, ipadx=5, ipady=5)
        buttons_dict[currentBtn].bind('<Button-1>', calculate)

# print(buttons_dict)

window.mainloop()