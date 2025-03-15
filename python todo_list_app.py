import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Create main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Create UI Elements
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
mark_button = tk.Button(root, text="Mark Completed", command=mark_completed)
task_listbox = tk.Listbox(root, width=50, height=15)

# Place UI Elements
task_entry.pack(pady=10)
add_button.pack()
task_listbox.pack(pady=10)
mark_button.pack()
remove_button.pack()

# Run the application
root.mainloop()