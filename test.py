import tkinter as tk
from tkinter import messagebox
import datetime


def log_data():
    name = name_entry.get().lower()
    task = task_var.get()
    file_name = f"{name}'s {task}.txt"
    info = data_entry.get()

    with open(file_name, 'a') as f:
        f.write(f"[{get_date()}] {info}\n")

    messagebox.showinfo("Success", "Data logged successfully!")


def retrieve_data():
    name = name_entry.get().lower()
    task = task_var.get()
    file_name = f"{name}'s {task}.txt"

    try:
        with open(file_name) as f:
            data = f.read()
            data_text.delete(1.0, tk.END)
            data_text.insert(tk.END, data)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")


def get_date():
    return datetime.datetime.now()


# Create the main window
root = tk.Tk()
root.title("HEALTH MANAGMENT SYSTEM")

# Create and configure widgets
name_label = tk.Label(root, text="Enter Your Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

task_label = tk.Label(root, text="Select Task:")
task_label.pack()
task_var = tk.StringVar(value="Food")
task_option_menu = tk.OptionMenu(root, task_var, "Food", "Exercise")
task_option_menu.pack()

data_label = tk.Label(root, text="Enter Data:")
data_label.pack()
data_entry = tk.Entry(root)
data_entry.pack()


log_button = tk.Button(root, text="Log Data", command=log_data)
log_button.pack()

retrieve_button = tk.Button(root, text="Retrieve Data", command=retrieve_data)
retrieve_button.pack()

data_text = tk.Text(root, height=10, width=40)
data_text.pack()

# Start the GUI main loop
root.mainloop()
