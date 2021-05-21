from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def Clear():
    e.delete(0, END)

def first_number(sign):
    a = e.get()
    global f_num
    f_num = float(a)
    global op
    op = sign
    e.delete(0, END)

def natures(nature):
    a = e.get()
    e.delete(0, END)
    global f_num
    if nature == "+/-":
        if a[0] == "-":
            a = e.insert(0, str(int(a)*-1))
        else:
            a = e.insert(0, "-" + str(a))
    elif nature == ".":
        if "." in a:
            a = e.insert(0, str(a))
        else:
            a = e.insert(0, str(a) + str(nature))
    

def equal():
    b = e.get()
    e.delete(0, END)
    if op == "+":
        e.insert(0, f_num + float(b))
    elif op == "-":
        e.insert(0, f_num - float(b))
    elif op == "x":
        e.insert(0, f_num * float(b))
    elif op == "/":
        e.insert(0, f_num / float(b))
    
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3)).grid(row=3, column=2)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6)).grid(row=2, column=2)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9)).grid(row=1, column=2)
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0)).grid(row=4, column=1)

button_negate = Button(root, text="+/-", padx=34, pady=20, command=lambda: natures("+/-")).grid(row=4, column=0)
button_comma = Button(root, text=".", padx=41, pady=20, command=lambda: natures(".")).grid(row=4, column=2)

button_plus = Button(root, text="+", padx=39, pady=20, command=lambda: first_number("+")).grid(row=1, column=4)
button_minus = Button(root, text="-", padx=40, pady=20, command=lambda: first_number("-")).grid(row=2, column=4)
button_times = Button(root, text="x", padx=40, pady=20, command=lambda: first_number("x")).grid(row=3, column=4)
button_divides = Button(root, text="/", padx=40, pady=20, command=lambda: first_number("/")).grid(row=4, column=4)
button_equal = Button(root, text="=", padx=134, pady=20, command=equal).grid(row=5, column=1, columnspan=4)
button_clear = Button(root, text="C", padx=39, pady=20, command=Clear).grid(row=5, column=0)

root.mainloop()