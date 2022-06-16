# Python GUI program to

from tkinter import *


def average():
    res = int(e1.get()) + int(e2.get()) + int(e3.get())/3
    label_text.set(res)

# def grade():
#     answer



# def sub_numbers():
#     res = int(e1.get()) - int(e2.get())
#     label_text.set(res)
#
#
# def mul_numbers():
#     res = int(e1.get()) * int(e2.get())
#     label_text.set(res)
#
#
# def div_numbers():
#     res = int(e1.get()) % int(e2.get())
#     label_text.set(res)


window = Tk()
label_text = StringVar();
label_text2 = StringVar;
Label(window, text="Enter Marks in Pysics:").grid(row=0, sticky=W)
Label(window, text="Enter Marks in Chemistry:").grid(row=2, sticky=W)
Label(window, text="Enter Marks in Maths:").grid(row=4, sticky=W)
Label(window, text="The average is:").grid(row=6, sticky=W)
Label(window, text="The grade is:").grid(row=8, sticky=W)
result = Label(window, text="", textvariable=label_text).grid(row=6, column=1, sticky=W)
result2 = Label(window, text="", textvariable=label_text2).grid(row=8, column=1, sticky=W)


e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

b = Button(window, text="Average", command=average)
b.grid(row=0, column=2, padx=5, pady=5)


# b = Button(window, text="sub", command=sub_numbers)
# b.grid(row=1, column=2, padx=5, pady=5)
#
# b = Button(window, text="mul", command=mul_numbers)
# b.grid(row=2, column=2, padx=5, pady=5)
#
# b = Button(window, text="div", command=div_numbers)
# b.grid(row=3, column=2, padx=5, pady=5)

mainloop()
