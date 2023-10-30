import tkinter as tk

# Function to perform arithmetic operations
def calculate():
    try:
        dig1 = float(entry_dig1.get())
        digi2 = float(entry_digi2.get())
        operation = operator.get()
        
        if operation == "+":
            result.set(dig1 + digi2)
        elif operation == "-":
            result.set(dig1 - digi2)
        elif operation == "*":
            result.set(dig1 * digi2)
        elif operation == "/":
            if digi2 == 0:
                result.set("Error")
            else:
                result.set(dig1 / digi2)
    except ValueError:
        result.set("Invalid Input")

# Create a tkinter window
window = tk.Tk()
window.title("Calculator")

# Input fields
entry_dig1 = tk.Entry(window)
entry_dig1.pack()
entry_digi2 = tk.Entry(window)
entry_digi2.pack()

# Dropdown for selecting the operation
operator = tk.StringVar()
operator.set("+")
dropdown = tk.OptionMenu(window, operator, "+", "-", "*", "/")
dropdown.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Result
result = tk.StringVar()
result.set("")
result_label = tk.Label(window, textvariable=result)
result_label.pack()

window.mainloop()