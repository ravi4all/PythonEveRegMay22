from tkinter import *

# initialize your window
window = Tk()
window.geometry('700x600')
window.title("My First GUI...")

# fg - foreground
# bg - background
label = Label(window, text = "My First GUI Application...", 
                font=('Arial',20), fg='red', bg='white')
# label.grid(row=0, column=0, padx=10, pady=10)
# label.pack(fill=BOTH)
label.place(x = 100, y = 50)

label = Label(window, text = "This is tkinter demo app...", 
                font=('Arial',20), fg='blue', bg='yellow')
# label.grid(row=1, column=0, padx=10, pady=10)
# label.pack(fill=BOTH)
label.place(x = 100, y = 100)

label = Label(window, text = "Tkinter is used for desktop app development",
                 font=('Arial',20), fg='green', bg='red')
# label.grid(row=1, column=1, padx=10, pady=10)
# label.pack(fill=BOTH)
label.place(x = 100, y = 150)

window.mainloop()