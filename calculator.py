import tkinter as tk
from math import sqrt, pow

def on_button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
            history.insert(tk.END, screen.get() + " = " + result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

def clear_history():
    history.delete(1.0, tk.END)

def square_root():
    try:
        num = float(screen.get())
        if num >= 0:
            result = sqrt(num)
            screen.set(result)
            history.insert(tk.END, "√" + str(num) + " = " + str(result))
        else:
            screen.set("Error")
    except Exception as e:
        screen.set("Error")

def exponentiate():
    try:
        expression = screen.get()
        if "^" in expression:
            base, power = expression.split("^")
            result = pow(float(base), float(power))
            screen.set(result)
            history.insert(tk.END, expression + " = " + str(result))
        else:
            screen.set("Error")
    except Exception as e:
        screen.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry field for input and display
screen = tk.StringVar()
entry_field = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry_field.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# Create the calculator buttons
button_frame = tk.Frame(root)
button_frame.pack()

button_labels = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/",
    "(", ")", "√", "^"
]

row, col = 0, 0

for label in button_labels:
    button = tk.Button(button_frame, text=label, font="lucida 15 bold", height=2, width=5)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# History log
history = tk.Text(root, height=5, width=30, font="lucida 12")
history.pack(pady=10)

# Clear history button
clear_button = tk.Button(root, text="Clear History", font="lucida 12 bold", command=clear_history)
clear_button.pack()

# Run the GUI event loop
root.mainloop()
