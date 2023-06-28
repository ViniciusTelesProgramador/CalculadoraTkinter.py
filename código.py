import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)
    
def evaluate_calculation():
    global calculation
    print(calculation)

    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0,"end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
        

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()

root.geometry("300x275")
root.title('CALCULADORA')



text_result = tk.Text(root, height=2, width=16, font=("Arial",24))
text_result.grid(columnspan=5)

bot1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
bot1.grid(row=2, column=1)

bot2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
bot2.grid(row=2, column=2)

bot3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
bot3.grid(row=2, column=3)

bot4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
bot4.grid(row=3, column=1)

bot5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
bot5.grid(row=3, column=2)

bot6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
bot6.grid(row=3, column=3)

bot7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
bot7.grid(row=4, column=1)

bot8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
bot8.grid(row=4, column=2)

bot9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
bot9.grid(row=4, column=3)

bot0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
bot0.grid(row=5, column=2)

bot_mais = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
bot_mais.grid(row=2, column=4)

bot_menos = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
bot_menos.grid(row=3, column=4)

bot_mult = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
bot_mult.grid(row=4, column=4)

bot_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
bot_div.grid(row=5, column=4)

bot_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
bot_open.grid(row=5, column=1)

bot_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
bot_close.grid(row=5, column=3)

bot_limpa = tk.Button(root, text="C", command = clear_field, width=11, font=("Arial", 14))
bot_limpa.grid(row=6, column=1, columnspan=2)

bot_igual = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
bot_igual.grid(row=6, column=3, columnspan=2)
root.mainloop()
