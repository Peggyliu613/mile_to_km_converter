from tkinter import *


window = Tk()
window.title("Mile to Kilogram Converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)

mile_inputted = Entry(width=5)
mile_inputted.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

convert_to = Label(text=0)
convert_to.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)


def calculate():
    convert_to["text"] = int(mile_inputted.get()) * 1.609

submit_button = Button(text="calculate", command=calculate)
submit_button.grid(column=1, row=2)


window.mainloop()