import tkinter as tk

# Function to perform arithmetic ops
def calculate():
    try:
        dig1 = float(entry_dig1.get())
        digi2 = float(entry_digi2.get())
        op = operator.get()
        
        if op == "+":
            result.set(dig1 + digi2)
        elif op == "-":
            result.set(dig1 - digi2)
        elif op == "*":
            result.set(dig1 * digi2)
        elif op == "/":
            if digi2 == 0:
                result.set("Error")
            else:
                result.set(dig1 / digi2)
    except ValueError:
        result.set("Invalid Input")

# Create a tkinter wd
wd = tk.Tk()
wd.title("Calculator")

# Input fields
entry_dig1 = tk.Entry(wd)
entry_dig1.pack()
entry_digi2 = tk.Entry(wd)
entry_digi2.pack()

# Dropdown for selecting the op
operator = tk.StringVar()
operator.set("+")
dropdown = tk.OptionMenu(wd, operator, "+", "-", "*", "/")
dropdown.pack()

# Calculate button
calculate_button = tk.Button(wd, text="Calculate", command=calculate)
calculate_button.pack()

# Result
result = tk.StringVar()
result.set("")
result_label = tk.Label(wd, textvariable=result)
result_label.pack()

wd.mainloop()