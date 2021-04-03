from tkinter import *

window = Tk()
window.title("Calculator")
t1 = Entry(window, borderwidth=3, width=42)

def button_add(number):
    current = t1.get()
    t1.delete(0, END)
    t1.insert(0, str(current) + str(number))


def clear():
    t1.delete(0, END)
    count = 0
    return count

def add():
    number = t1.get()
    global first_num
    global math
    math = "add"
    first_num = int(number)
    t1.delete(0, END)

def subtract():
    number = t1.get()
    global first_num
    global math
    math = "sub"
    first_num = int(number)
    t1.delete(0, END)

def multiply():
    number = t1.get()
    global first_num
    global math
    math = "mult"
    first_num = int(number)
    t1.delete(0, END)


def division():
    number = t1.get()
    global first_num
    global math
    math = "div"
    first_num = int(number)
    t1.delete(0, END)

def equals():
    if math == "mult":
        second_number = t1.get() 
        t1.delete(0, END)
        t1.insert(0, int(first_num) * int(second_number))
    if math == "div":
        second_number = t1.get() 
        t1.delete(0, END)
        if int(second_number) == 0:
            t1.insert(0,"Error")
        else:
            t1.insert(0, float(first_num) / float(second_number))
    if math == "add":
        second_number = t1.get() 
        t1.delete(0, END)
        t1.insert(0, int(first_num) + int(second_number))
    if math == "sub":
        second_number = t1.get() 
        t1.delete(0, END)
        t1.insert(0, int(first_num) - int(second_number))

#define the buttons for calculator
divide_btn = Button(window, text="÷", padx=40, pady=20, command=division)
multiply_btn = Button(window, text="x", padx=40, pady=20, command=multiply)
subtract_btn = Button(window, text="-", padx=40, pady=20, command=subtract)
add_btn = Button(window, text="+", padx=40, pady=20, command=add)
equals_btn = Button(window, text="=", padx=40, pady=20, command=equals)
clear_btn = Button(window, text = "c", padx=40, pady=20, command=clear)
btn0 = Button(window, text = "0", padx=136, pady=20, command=lambda: button_add(0))
btn1 = Button(window, text = "1", padx=40, pady=20, command=lambda: button_add(1))
btn2 = Button(window, text = "2", padx=40, pady=20, command=lambda: button_add(2))
btn3 = Button(window, text = "3", padx=40, pady=20, command=lambda: button_add(3))
btn4 = Button(window, text = "4", padx=40, pady=20, command=lambda: button_add(4))
btn5 = Button(window, text = "5", padx=40, pady=20, command=lambda: button_add(5))
btn6 = Button(window, text = "6", padx=40, pady=20, command=lambda: button_add(6))
btn7 = Button(window, text = "7", padx=40, pady=20, command=lambda: button_add(7))
btn8 = Button(window, text = "8", padx=40, pady=20, command=lambda: button_add(8))
btn9 = Button(window, text = "9", padx=40, pady=20, command=lambda: button_add(9))
        
#define button placement
equals_btn.grid(row=5, column=3)
btn0.grid(row=5, column=0, columnspan=3)
add_btn.grid(row=4, column=3)
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
subtract_btn.grid(row=3, column=3)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
multiply_btn.grid(row=2, column=3)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
clear_btn.grid(row=1, column=2)
divide_btn.grid(row=1, column=3)
t1.grid(row=0, column=0, columnspan=4, ipady=10)


window.resizable(0, 0)
window.geometry("400x380")
window.mainloop()
