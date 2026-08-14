# Virtual Inventory

A desktop inventory management application built with Python and Tkinter. The application provides a graphical interface for adding, viewing, and removing inventory items while keeping item quantities synchronized across the interface.

This was one of my first software projects and served as an introduction to Python application development, GUI programming, and managing application state.

## Features

- **View Inventory** — Displays all current inventory items and their quantities
- **Add Items** — Adds new items and quantities through the graphical interface
- **Remove Items** — Allows users to select and remove existing inventory items
- **Dynamic Updates** — Updates the inventory display and item selection list whenever the inventory changes
- **Duplicate Item Handling** — Updates the quantity of an existing item instead of creating a duplicate entry
- **Basic Input Validation** — Rejects non-integer quantities and prevents item removal when no item is selected

## Technologies

- Python
- Tkinter

## Project Structure

```text
virtual-inventory/
├── src/
│   └── inventory.py
├── .gitignore
└── README.md
```

## Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/JaredSantiago-code/virtual-inventory.git
cd virtual-inventory
```

### 2. Ensure Python 3 and Tkinter are installed

Tkinter is included with many Python installations. On Debian/Ubuntu systems, it can be installed with:

```bash
sudo apt-get install python3-tk
```

### 3. Run the application

```bash
python3 src/inventory.py
```

## Screenshots

### Empty Inventory

<img width="470" alt="Virtual Inventory empty state" src="https://github.com/user-attachments/assets/ad8bd09c-1b8d-4278-996a-0b7b774e0ecd">

### Inventory with Items

<img width="470" alt="Virtual Inventory populated with items" src="https://github.com/user-attachments/assets/bc7290b9-5882-4ace-8848-0c2a1a9a5fe3">
