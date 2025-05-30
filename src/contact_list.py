from tkinter import *
from tkinter import messagebox
from pandas import DataFrame,errors,read_csv
from functools import partial as p

app = Tk()

def contact_list(tkinter_app):
    main = Toplevel(tkinter_app)
    main.title("Contact List")

    with open("contacts.csv","w") as f:
        f.close()
    while True:
        try:
            contacts = read_csv("contacts.csv").to_dict(orient="records")
            break
        except FileNotFoundError:
            with open("contacts.csv", "w") as f:
                f.close()
        except errors.EmptyDataError:
            contacts = []
            break
    contacts_dataframe = DataFrame(contacts, columns=["name", "phone", "email"])


    title_label = Label(main, text="Contact List")
    title_label.grid(row=0, column=0)



    def update(idx):
        contact = contacts[idx]
        update_window = Toplevel(main)
        update_window.title("Update Contact")
        name_entry = Entry(update_window)
        name_entry.insert(0, contact["name"])
        phone_entry = Entry(update_window)
        phone_entry.insert(0, contact["phone"])
        email_entry = Entry(update_window)
        email_entry.insert(0, contact["email"])
        Label(update_window, text="Name").grid(row=0, column=0)
        Label(update_window, text="Phone Number").grid(row=1, column=0)
        Label(update_window, text="Email").grid(row=2, column=0)
        name_entry.grid(row=0, column=1)
        phone_entry.grid(row=1, column=1)
        email_entry.grid(row=2, column=1)
        def submit():
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            try:
                contacts[idx] = {"name": name, "phone": phone, "email": email}
                contacts_dataframe = DataFrame(contacts, columns=["name", "phone", "email"])
                contacts_dataframe.to_csv("contacts.csv", index=False)
                messagebox.showinfo("Success", "Contact updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update contact: {e}")
            finally:
                refresh()
                update_window.destroy()
        Button(update_window, text="Submit", command=submit).grid(row=3, column=0)


    def delete(idx):
        try:
            contact = contacts[idx]
            if messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {contact['name']}?"):
                contacts.pop(idx)
                contacts_dataframe = DataFrame(contacts, columns=["name", "phone", "email"])
                contacts_dataframe.to_csv("contacts.csv", index=False)
                messagebox.showinfo("Success", "Contact deleted successfully")
                refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete contact: {e}")


    def create():
        def submit():
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            try:
                contacts.append({"name": name, "phone": phone, "email": email})
                contacts_dataframe = DataFrame(contacts, columns=["name", "phone", "email"])
                contacts_dataframe.to_csv("contacts.csv", index=False)
                messagebox.showinfo("Success", "Contact created successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create contact: {e}")
            finally:
                refresh()
                create_window.destroy()
        create_window = Toplevel(main)
        create_window.title("Create Contact")
        Label(create_window, text="Name").grid(row=0, column=0)
        Label(create_window, text="Phone Number").grid(row=1, column=0)
        Label(create_window, text="Email").grid(row=2, column=0)
        name_entry = Entry(create_window)
        phone_entry = Entry(create_window)
        email_entry = Entry(create_window)
        name_entry.grid(row=0, column=1)
        phone_entry.grid(row=1, column=1)
        email_entry.grid(row=2, column=1)
        Button(create_window, text="Submit", command=submit).grid(row=3, column=0)
        Button(create_window, text="Cancel", command=create_window.destroy).grid(row=3, column=1)


    def refresh():
        global b
        for widget in main.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()
        for idx, contact in enumerate(contacts):
            Label(main, text=f"{idx + 1}").grid(row=idx + 1, column=0)
            Label(main, text=f"Name  : {contact['name']}").grid(row=idx + 1, column=1)
            Label(main, text=f"Phone Number : {contact['phone']}").grid(row=idx + 1, column=2)
            Label(main, text=f"Email : {contact['email']}").grid(row=idx + 1, column=3)
            ub = Button(main, text="Update", command=lambda i=idx: update(i))
            ub.grid(row=idx + 1, column=4)
            db = Button(main, text="Delete", command=lambda i=idx: delete(i))
            db.grid(row=idx + 1, column=5)
        b = Button(main, text="Create", command=create)
        b.grid(row=len(contacts) + 1, column=0, columnspan=2)

    refresh()
    main.mainloop()

if __name__ = "__main__" :
    contact_list(app)
