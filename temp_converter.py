import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        temp = float(entry.get())
        if var.get() == "C to F":
            result = (temp * 9/5) + 32
            output_label.config(text=f"{result:.2f} °F")
        else:
            result = (temp - 32) * 5/9
            output_label.config(text=f"{result:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI window
root = tk.Tk()
root.title("Temperature Converter")

# Entry and Radio Buttons
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=1, padx=10, pady=10)

var = tk.StringVar(value="C to F")
tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value="C to F").grid(row=1, column=0, columnspan=2)
tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value="F to C").grid(row=2, column=0, columnspan=2)

# Convert button
tk.Button(root, text="Convert", command=convert).grid(row=3, column=0, columnspan=2, pady=10)

# Output label
output_label = tk.Label(root, text="")
output_label.grid(row=4, column=0, columnspan=2)

root.mainloop()