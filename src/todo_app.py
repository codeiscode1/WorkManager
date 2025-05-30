from tkinter import *
from tkinter import messagebox
from pandas import DataFrame,errors,read_csv
app_main = Tk()
app_main.title("Todo List")
Label(app_main,text = f"Todo List").grid(row=0, column=0)

while True:
    try:
        todos = read_csv("todos.csv").to_dict(orient="records")
        break
    except FileNotFoundError:
        with open("todos.csv", "w") as f:
            f.close()
    except errors.EmptyDataError:
        todos = []
        break



def refresh():
    for widget in app_main.winfo_children():
        widget.destroy()
    Label(app_main, text="Todo List").grid(row=0, column=0)
    for id,contact in enumerate(todos):
        Label(app_main,text = f"Title:{contact["title"]}").grid(row=id+1, column=0)
        Label(app_main,text = f"Description:{contact['description']}").grid(row=id+1, column=1)
        Label(app_main,text = f"Status:{contact['status']}").grid(row=id+1, column=2)
        cb = Button(app_main, text="Change Status")
        cb.grid(row=id+1, column=3)
        cb.config(command=lambda id=id: change_status(id))
        db = Button(app_main, text="Delete")
        db.grid(row=id+1, column=4)
        db.config(command=lambda id=id: delete(id))
    create_button = Button(app_main, text="Create Todo", command=create)
    create_button.grid(row=len(todos) + 1, column=5)
def create():
    def submit():
        title = title_entry.get()
        description = description_entry.get()
        status = status_entry.get()
        if title and description and status:
            todos.append({"title": title, "description": description, "status": status})
            DataFrame(todos).to_csv("todos.csv")
            messagebox.showinfo("Success", "Todo created successfully!")
            create_window.destroy()
            refresh()
    create_window = Toplevel(app_main)
    create_window.title("Create Todo")
    Label(create_window, text="Title:",anchor = "w").grid(row=0, column=0)
    title_entry = Entry(create_window)
    title_entry.grid(row=0, column=1)
    Label(create_window, text="Description:",anchor = "w").grid(row=1, column=0)
    description_entry = Entry(create_window)
    description_entry.grid(row=1, column=1)
    Label(create_window, text="Status:",anchor = "w").grid(row=2, column=0)
    status_entry = Entry(create_window)
    status_entry.grid(row=2, column=1)
    Button(create_window, text="Save", command=submit).grid(row=3, column=0, columnspan=2)
    create_window.mainloop()
def change_status(id):
    global todos
    status = Toplevel(app_main)
    status.title("Change Status")
    Label(status, text="New Status:").grid(row=0, column=0)
    status_entry = Entry(status)
    status_entry.grid(row=0, column=1)
    def submit():
        new_status = status_entry.get()
        if new_status:
            todos[id]["status"] = new_status
            DataFrame(todos).to_csv("todos.csv")
            status.destroy()
            messagebox.showinfo("Success", "Status updated successfully!")
            refresh()
    Button(status, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)
    status.mainloop()
    pass
def delete(id):
    global todos
    todos.pop(id)
    DataFrame(todos).to_csv("todos.csv", index=False)
    messagebox.showinfo("Success", "Todo deleted successfully!")
    refresh()
    pass


for id,contact in enumerate(todos):
    Label(app_main,text = f"Title:{contact["title"]}").grid(row=id+1, column=0)
    Label(app_main,text = f"Description:{contact['description']}").grid(row=id+1, column=1)
    Label(app_main,text = f"Status:{contact['status']}").grid(row=id+1, column=2)
    cb = Button(app_main, text="Change Status")
    cb.grid(row=id+1, column=3)
    cb.config(command=lambda id=id: change_status(id))
    db = Button(app_main, text="Delete")
    db.grid(row=id+1, column=4)
    db.config(command=lambda id=id: delete(id))
create_button = Button(app_main, text="Create Todo", command=create)
create_button.grid(row=len(todos) + 1, column=5)

app_main.mainloop()
