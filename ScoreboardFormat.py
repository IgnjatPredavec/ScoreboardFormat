import tkinter as tk
from tkinter import scrolledtext, messagebox
import json

def format_data(data):
    formatted_output = ""
    for index, item in enumerate(data):
        formatted_output += f"{index}:\n"
        formatted_output += f"name: {item.get('name', '')}\n"
        formatted_output += f"score: {item.get('score', '')}\n\n"
    return formatted_output

def process_data():
    input_data = input_text.get("1.0", "end-1c").strip()
    try:
        data = json.loads(input_data)
        formatted_output = format_data(data)
        output_text.delete("1.0", "end")
        output_text.insert("1.0", formatted_output)
    except json.JSONDecodeError as e:
        messagebox.showerror("Error", f"Invalid JSON data:\n{str(e)}")

# Create the main application window
root = tk.Tk()
root.title("JSON Formatter App")
root.geometry("600x400")

# Instructions Label
instructions_label = tk.Label(root, text="Copy and paste your JSON data below:")
instructions_label.pack(pady=10)

# Input Text Area
input_text = scrolledtext.ScrolledText(root, width=70, height=10)
input_text.pack(pady=10)

# Format Button
format_button = tk.Button(root, text="Format Data", command=process_data)
format_button.pack(pady=10)

# Output Text Area
output_text = scrolledtext.ScrolledText(root, width=70, height=15)
output_text.pack(pady=10)

# Start the GUI main loop
root.mainloop()
