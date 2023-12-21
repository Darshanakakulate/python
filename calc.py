import tkinter as tk

def on_button_click(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        else:
            result = "Error"
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error")
root = tk.Tk()
root.title("Simple Calculator")
entry1_label = tk.Label(root, text="Enter number 1:")
entry1_label.grid(row=0, column=0)
entry1 = tk.Entry(root, width=15, font=('Arial', 14))
entry1.grid(row=0, column=1)

entry2_label = tk.Label(root, text="Enter number 2:")
entry2_label.grid(row=1, column=0)
entry2 = tk.Entry(root, width=15, font=('Arial', 14))
entry2.grid(row=1, column=1)
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=2)
operators = ['+', '-', '*', '/', '%']
row_val = 3
col_val = 0
for operator in operators:
    tk.Button(root, text=operator, width=5, height=2,
              command=lambda op=operator: on_button_click(op)).grid(row=row_val, column=col_val)
    col_val += 1
root.mainloop()
