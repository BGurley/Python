from tkinter import *

kmNum=0

Button
def button_clicked():
    kmNum = (int(input.get()) * 1.60934)
    KmNumLabel.config(text=kmNum)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=10, pady=10)

# Label
my_label = Label(text="Miles", font=("Arial", 10))
my_label.grid(column=6, row=0)
my_label.config(padx=10, pady=10)

# is equal to Label
equals = Label(text="is equal to", font=("Arial", 10))
equals.grid(column=0, row=2)
equals.config(padx=10, pady=10)

# km number label
KmNumLabel = Label(text=kmNum, font=("Arial", 10))
KmNumLabel.grid(column=3, row=2)
KmNumLabel.config(padx=10, pady=10)

# km Label
KmLabel = Label(text="Km", font=("Arial", 10))
KmLabel.grid(column=6, row=2)
KmLabel.config(padx=10, pady=10)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=3, row=6)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=0)

window.mainloop()