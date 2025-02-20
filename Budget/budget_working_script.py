import os
import tkinter as tk
from tkinter import ttk
import datetime
import pandas as pd

# Get current month
current_month = datetime.datetime.now().strftime("%m")

# Load existing data from Excel if available
try:
    existing_sheet = pd.read_excel("excel_budget.xlsx", sheet_name=current_month, engine="openpyxl")
except (FileNotFoundError, ValueError):
    existing_sheet = pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"])

def add_expense():
    global existing_sheet  
    date_input = date_entry.get().strip()
    
    # Use provided date or default to today
    try:
        date = datetime.datetime.strptime(date_input, "%d-%b").strftime("%d-%b") if date_input else datetime.datetime.now().strftime("%d-%b")
    except ValueError:
        status_label.config(text="Invalid date! Use format: DD-MMM (e.g., 15-Feb)", fg="red")
        return

    name = name_entry.get() or " "
    rent = rent_entry.get() or "0"
    need = need_entry.get() or "0"
    transit = transit_entry.get() or "0"
    luxury = luxury_entry.get() or "0"
    lent = lent_entry.get() or "0"
    savings = savings_entry.get() or "0"

    # Create new row
    new_row = pd.DataFrame([{
        "Date": date, "Name": name, "Rent": rent, "Need": need, 
        "Transit": transit, "Luxury": luxury, "Lent": lent, "Savings": savings
    }])

    # Read existing data
    try:
        existing_sheet = pd.read_excel("excel_budget.xlsx", sheet_name=current_month, engine="openpyxl")
    except (FileNotFoundError, ValueError):
        existing_sheet = pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"])

    # Append new data
    updated_sheet = pd.concat([existing_sheet, new_row], ignore_index=True)

    # Write back to Excel (overwrite the sheet)
    with pd.ExcelWriter("excel_budget.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        updated_sheet.to_excel(writer, sheet_name=current_month, index=False)

    status_label.config(text="Expense added successfully!", fg="green")
    clear_expenses()
    view_expenses()

def delete_expense():
    global existing_sheet
    selected_item = expenses_tree.selection()
    if selected_item:
        item_text = expenses_tree.item(selected_item, "values")
        date, name, rent, need, transit, luxury, lent, savings = item_text

        # Load updated data from Excel
        try:
            existing_sheet = pd.read_excel("excel_budget.xlsx", sheet_name=current_month, engine="openpyxl")
        except (FileNotFoundError, ValueError):
            existing_sheet = pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"])

        # Filter out the selected row
        existing_sheet = existing_sheet[
            ~((existing_sheet.Date == date) & (existing_sheet.Name == name))
        ]

        # Save updated sheet
        with pd.ExcelWriter("excel_budget.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            existing_sheet.to_excel(writer, sheet_name=current_month, index=False)

        status_label.config(text="Expense deleted successfully!", fg="green")
        view_expenses()
    else:
        status_label.config(text="Please select an expense to delete!", fg="red")

def view_expenses():
    global expenses_tree
    total_expense = 0
    expenses_tree.delete(*expenses_tree.get_children())

    # Read data from Excel
    try:
        existing_sheet = pd.read_excel("excel_budget.xlsx", sheet_name=current_month, engine="openpyxl")
    except (FileNotFoundError, ValueError):
        existing_sheet = pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"])

    # Populate Treeview with data
    for _, row in existing_sheet.iterrows():
        values = row.tolist()
        expenses_tree.insert("", tk.END, values=values)
        try:
            total_expense += sum(int(v) if str(v).isdigit() else 0 for v in values[2:])
        except ValueError:
            pass

    total_label.config(text=f"Total Expense: {total_expense:.2f}")

def clear_expenses():
    date_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    rent_entry.delete(0, tk.END)
    need_entry.delete(0, tk.END)
    transit_entry.delete(0, tk.END)
    luxury_entry.delete(0, tk.END)
    lent_entry.delete(0, tk.END)
    savings_entry.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Expense Tracker")

# Date entry
date_label = tk.Label(root, text="Date (DD-MMM):")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=5, pady=5)

# Expense name entry
name_label = tk.Label(root, text="Expense Name:")
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=5, pady=5)

# Categories
categories = ["Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]
entries = {}
for idx, category in enumerate(categories, start=2):
    tk.Label(root, text=f"{category}:").grid(row=idx, column=0, padx=5, pady=5)
    entry = tk.Entry(root, textvariable=tk.StringVar(value="0"))
    entry.grid(row=idx, column=1, padx=5, pady=5)
    entries[category.lower()] = entry

rent_entry, need_entry, transit_entry, luxury_entry, lent_entry, savings_entry = [entries[cat] for cat in ["rent", "need", "transit", "luxury", "lent", "savings"]]

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10)

columns = ("Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings")
expenses_tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    expenses_tree.heading(col, text=col)
expenses_tree.grid(row=9, column=0, columnspan=3, padx=5, pady=5)

total_label = tk.Label(root, text="")
total_label.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

view_button = tk.Button(root, text="View Expenses", command=view_expenses)
view_button.grid(row=12, column=0, padx=5, pady=10)

delete_button = tk.Button(root, text="Delete Expense", command=delete_expense)
delete_button.grid(row=13, column=1, padx=5, pady=10)

view_expenses()
root.mainloop()