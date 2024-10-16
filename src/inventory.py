import tkinter as tk
from tkinter import messagebox

# Virtual Inventory Management System with Tkinter GUI

# Initial Inventory (for demo purposes)
inventory = []

# Function to display all items in the inventory
def display_inventory():
    inventory_text.delete(1.0, tk.END)  # Clear the current content
    if not inventory:
        inventory_text.insert(tk.END, "Inventory is currently empty.\n")
    else:
        inventory_text.insert(tk.END, "Current Inventory:\n")
        for i, item in enumerate(inventory, 1):
            inventory_text.insert(tk.END, f"{i}. {item['name']} - Quantity: {item['quantity']}\n")

# Function to update the Listbox for removing items
def update_item_listbox():
    item_listbox.delete(0, tk.END)  # Clear the current listbox
    for item in inventory:
        item_listbox.insert(tk.END, f"{item['name']} - {item['quantity']}")

# Function to add a new item to the inventory
def add_item():
    name = name_entry.get().strip()
    try:
        quantity = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid quantity (integer).")
        return

    # Check if the item already exists in the inventory
    for item in inventory:
        if item['name'].lower() == name.lower():
            item['quantity'] += quantity
            messagebox.showinfo("Item Updated", f"Updated {name}'s quantity to {item['quantity']}.")
            display_inventory()
            update_item_listbox()
            return
    
    # If item is new, add it to the inventory
    inventory.append({"name": name, "quantity": quantity})
    messagebox.showinfo("Item Added", f"{name} added to the inventory with quantity {quantity}.")
    display_inventory()
    update_item_listbox()  # Update the Listbox after adding an item

# Function to remove an item from the inventory
def remove_item():
    try:
        selected_index = int(item_listbox.curselection()[0])  # Get the index of the selected item
        removed_item = inventory.pop(selected_index)
        messagebox.showinfo("Item Removed", f"{removed_item['name']} has been removed from the inventory.")
        display_inventory()
        update_item_listbox()  # Update the Listbox after removing an item
    except IndexError:
        messagebox.showerror("Error", "Please select an item to remove.")

# Main Application Window
root = tk.Tk()
root.title("Virtual Inventory System")

# Section to display the inventory
inventory_label = tk.Label(root, text="Inventory:")
inventory_label.pack()

inventory_text = tk.Text(root, height=10, width=50)
inventory_text.pack()

# Section to add items to the inventory
name_label = tk.Label(root, text="Item Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack()

# Section to remove items from the inventory
remove_label = tk.Label(root, text="Select Item to Remove:")
remove_label.pack()

item_listbox = tk.Listbox(root)
item_listbox.pack()

remove_button = tk.Button(root, text="Remove Item", command=remove_item)
remove_button.pack()

# Update the inventory display initially
display_inventory()
update_item_listbox()

# Run the main application loop
root.mainloop()
