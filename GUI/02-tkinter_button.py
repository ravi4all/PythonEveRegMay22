from tkinter import *

# initialize your window
window = Tk()
window.geometry('700x600')
window.title("My First GUI...")

def greet():
    # print("Hello", textBox.get())
    label_3.configure(text="Hello " + textBox.get())

# fg - foreground
# bg - background
label_1 = Label(window, text = "Greet Application", 
                font=('Arial',20), fg='red', bg='white')
label_1.place(x = 300, y = 50)

label_2 = Label(window, text = "Enter your name", 
                font=('Arial',20), fg='blue')
label_2.place(x = 100, y = 150)

# Textbox
textBox = Entry(window, width=20, font=('Arial',20))
textBox.place(x = 350, y = 150)

btn = Button(window, text="Greet", font=('Arial',20), width=20, command=greet)
btn.place(x = 200, y = 220)


label_3 = Label(window, text = "",
                 font=('Arial',20), fg='green')
label_3.place(x = 100, y = 300)

window.mainloop()