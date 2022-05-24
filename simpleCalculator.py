import tkinter as tk
import math

calculator = ""


def evaluate_calculation():
    global calculator
    try:
        calculator = str(eval(calculator))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculator)
    except:
        clear_all()
        text_result.insert(1.0, "Error")


def calculator_operands(symbol):
    global calculator
    calculator += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculator)


def clear_all():
    global calculator
    calculator = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.title("Calculator")
root.geometry("350x377")

text_result = tk.Text(root, height=2, width=19, font=("Arial", 24))
text_result.grid(columnspan=5)

#==================== ROW 2 ========================

button_clear = tk.Button(root, text="C", command=clear_all, height=2, width=7, font=("Arial", 14))
button_clear.grid(row=2, column=1)

button_open_bracket = tk.Button(root, text="(", command=lambda: calculator_operands("("), height=2, width=7, font=("Arial", 14))
button_open_bracket.grid(row=2, column=2)

button_close_bracket = tk.Button(root, text=")", command=lambda: calculator_operands(")"), height=2, width=7, font=("Arial", 14))
button_close_bracket.grid(row=2, column=3)

button_plus = tk.Button(root, text="+", command=lambda: calculator_operands("+"), height=2, width=7, font=("Arial", 14))
button_plus.grid(row=2, column=4)

#==================== ROW 3 ========================

button_7 = tk.Button(root, text="7", command=lambda: calculator_operands(7), height=2, width=7, font=("Arial", 14))
button_7.grid(row=3, column=1)

button_8 = tk.Button(root, text="8", command=lambda: calculator_operands(8), height=2, width=7, font=("Arial", 14))
button_8.grid(row=3, column=2)

button_9 = tk.Button(root, text="9", command=lambda: calculator_operands(9), height=2, width=7, font=("Arial", 14))
button_9.grid(row=3, column=3)

button_minus = tk.Button(root, text="-", command=lambda: calculator_operands("-"), height=2, width=7, font=("Arial", 14))
button_minus.grid(row=3, column=4)

#==================== ROW 4 ========================

button_4 = tk.Button(root, text="4", command=lambda: calculator_operands(4), height=2, width=7, font=("Arial", 14))
button_4.grid(row=4, column=1)

button_5 = tk.Button(root, text="5", command=lambda: calculator_operands(5), height=2, width=7, font=("Arial", 14))
button_5.grid(row=4, column=2)

button_6 = tk.Button(root, text="6", command=lambda: calculator_operands(6), height=2, width=7, font=("Arial", 14))
button_6.grid(row=4, column=3)

button_multiply = tk.Button(root, text="*", command=lambda: calculator_operands("*"), height=2, width=7, font=("Arial", 14))
button_multiply.grid(row=4, column=4)

#==================== ROW 5 ========================

button_1 = tk.Button(root, text="1", command=lambda: calculator_operands(1), height=2, width=7, font=("Arial", 14))
button_1.grid(row=5, column=1)

button_2 = tk.Button(root, text="2", command=lambda: calculator_operands(2), height=2, width=7, font=("Arial", 14))
button_2.grid(row=5, column=2)

button_3 = tk.Button(root, text="3", command=lambda: calculator_operands(3), height=2, width=7, font=("Arial", 14))
button_3.grid(row=5, column=3)

button_divide = tk.Button(root, text="/", command=lambda: calculator_operands("/"), height=2, width=7, font=("Arial", 14))
button_divide.grid(row=5, column=4)

#==================== ROW 6 ========================

button_dot = tk.Button(root, text=".", command=lambda: calculator_operands("."), height=2, width=7, font=("Arial", 14))
button_dot.grid(row=6, column=1)

button_zero = tk.Button(root, text="0", command=lambda: calculator_operands(0), height=2, width=7, font=("Arial", 14))
button_zero.grid(row=6, column=2)

button_equal_sign = tk.Button(root, text="=", command=evaluate_calculation, bg="#ADD8E6", height=2, width=15, font=("Arial", 14))
button_equal_sign.grid(row=6, column=3, columnspan=2)






root.mainloop()