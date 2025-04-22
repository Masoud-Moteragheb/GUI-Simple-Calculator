import tkinter as tk

# Function to handle button clicks
def click(event):
    global expression
    text = event.widget["text"]
    if text == "=":
        try:
            result = str(eval(expression))
            entry_var.set(result)
            expression = result  # For continuing calculations
        except Exception:
            entry_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

# Initialize the app window
root = tk.Tk()
root.title("Simple Calculator")

# Display area
expression = ""
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Helvetica 20", justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, padx=10, pady=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Create buttons dynamically
for row in buttons:
    frame = tk.Frame(root)
    for btn in row:
        b = tk.Button(frame, text=btn, font="Helvetica 18", width=5, height=2)
        b.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        b.bind("<Button-1>", click)
    frame.pack(expand=True, fill="both")

# Start the GUI event loop
root.mainloop()
