from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")

        # Add widgets
        self.task_var = StringVar()

        self.entry = Entry(self.root, textvariable=self.task_var, font=('Arial', 14))
        self.entry.pack(pady=10)

        self.add_btn = Button(self.root, text="Add Task", command=self.add_task)
        self.add_btn.pack()

        self.listbox = Listbox(self.root, font=('Arial', 14), width=40, height=10)
        self.listbox.pack(pady=10)

        self.delete_btn = Button(self.root, text="Delete Selected Task", command=self.delete_task)
        self.delete_btn.pack()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.listbox.insert(END, task)
            self.task_var.set("")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected[0])

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
