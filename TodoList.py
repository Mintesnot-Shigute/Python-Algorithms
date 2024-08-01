import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
from datetime import datetime

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fancy To-Do List")

        self.tasks = []
        self.task_var = tk.StringVar()
        self.priority_var = tk.StringVar()
        self.due_date_var = tk.StringVar()

        # Entry for
        task_label = tk.Label(root, text="Task:")
        task_label.grid(row=0, column=0, padx=5, pady=5)
        self.task_entry = tk.Entry(root, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        # Priority dropdown
        priority_label = tk.Label(root, text="Priority:")
        priority_label.grid(row=0, column=2, padx=5, pady=5)
        priorities = ["Low", "Medium", "High"]
        self.priority_combobox = ttk.Combobox(root, textvariable=self.priority_var, values=priorities)
        self.priority_combobox.grid(row=0, column=3, padx=5, pady=5)
        self.priority_combobox.set("Medium")

        # Due date entry
        due_date_label = tk.Label(root, text="Due Date:")
        due_date_label.grid(row=0, column=4, padx=5, pady=5)
        self.due_date_entry = tk.Entry(root, textvariable=self.due_date_var, width=15)
        self.due_date_entry.grid(row=0, column=5, padx=5, pady=5)

        # Buttons for actions
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=6, padx=5, pady=5)

        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=0, column=7, padx=5, pady=5)

        view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        view_button.grid(row=0, column=8, padx=5, pady=5)

    def add_task(self):
        task = self.task_var.get()
        priority = self.priority_var.get()
        due_date_str = self.due_date_var.get()

        if task:
            due_date = self.parse_due_date(due_date_str)
            self.tasks.append({"Task": task, "Priority": priority, "Due Date": due_date})
            messagebox.showinfo("Task Added", f'Task "{task}" added.')
            self.clear_entry_fields()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def remove_task(self):
        task = self.task_var.get()
        if task in [task_info["Task"] for task_info in self.tasks]:
            self.tasks = [task_info for task_info in self.tasks if task_info["Task"] != task]
            messagebox.showinfo("Task Removed", f'Task "{task}" removed.')
            self.clear_entry_fields()
        else:
            messagebox.showwarning("Task Not Found", f'Task "{task}" not found.')

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks in the to-do list.")
        else:
            tasks_text = "\n".join([f"{i + 1}. Task: {task_info['Task']}, Priority: {task_info['Priority']}, Due Date: {task_info['Due Date']}" for i, task_info in enumerate(self.tasks)])
            messagebox.showinfo("To-Do List", tasks_text)

    def clear_entry_fields(self):
        self.task_var.set("")
        self.priority_combobox.set("Medium")
        self.due_date_var.set("")

    def parse_due_date(self, due_date_str):
        try:
            return datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            return None

def main():
    root = tk.Tk()
    style = ThemedStyle(root)
    style.set_theme("arc")  # Choose a theme, e.g., "plastik", "clearlooks", "arc", etc.
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
