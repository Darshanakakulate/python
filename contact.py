
import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = {'darshana': '1234567890', 'kunal': '9876543210'}

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.contacts_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.contacts_listbox.grid(row=5, column=0, columnspan=2, pady=10)
        self.update_listbox()

    def update_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.contacts_listbox.insert(tk.END, f"{name}: {phone}")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            self.contacts[name] = phone
            self.update_listbox()
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
        else:
            messagebox.showwarning("Warning", "Name and phone cannot be empty!")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts_listbox.get(selected_index)
            old_name, old_phone = selected_contact.split(": ")
            new_name = self.name_entry.get()
            new_phone = self.phone_entry.get()

            if new_name and new_phone:
                del self.contacts[old_name]
                self.contacts[new_name] = new_phone
                self.update_listbox()
                messagebox.showinfo("Success", f"Contact updated successfully!")
            else:
                messagebox.showwarning("Warning", "Name and phone cannot be empty!")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update!")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts_listbox.get(selected_index)
            name, _ = selected_contact.split(": ")
            del self.contacts[name]
            self.update_listbox()
            messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
