import os
import tkinter as tk
from tkinter import ttk
import datetime
import pandas as pd

current_month = datetime.datetime.now().strftime("%m")
print(current_month)
print(type(current_month))

try:
    existing_sheet = pd.read_excel("excel_budget.xlsx", sheet_name=current_month, engine="openpyxl")
except (FileNotFoundError, ValueError):
    existing_sheet = pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"])

start_row = existing_sheet.shape[0] + 1  # +1 to start after last row
print(start_row)

def add_expense():
    global existing_sheet  # Ensure modifications persist
    date    = datetime.datetime.now().strftime("%d-%b")
    print(date)
    name    = name_entry.get() or "Unknown"
    rent    = rent_entry.get() or "0"
    need    = need_entry.get() or "0"
    transit = transit_entry.get() or "0"
    luxury  = luxury_entry.get() or "0"
    lent    = lent_entry.get() or "0"
    savings = savings_entry.get() or "0"

    # Append new entry to text file
    with open("expenses.txt", "a") as file:
        file.write(f"{date},{name},{rent},{need},{transit},{luxury},{lent},{savings}\n")

    # Append to existing DataFrame
    new_row = {"Date":date, "Name":name, "Rent":rent, "Need":need, "Transit":transit, "Luxury":luxury, "Lent":lent, "Savings":savings }
    existing_sheet.loc[len(existing_sheet)] = new_row
    #print("------------")
    #print(existing_sheet)


    status_label.config(text="Expense added successfully!", fg="green")
    date_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    rent_entry.delete(0, tk.END)
    need_entry.delete(0, tk.END)
    transit_entry.delete(0, tk.END)
    luxury_entry.delete(0, tk.END)
    lent_entry.delete(0, tk.END)
    savings_entry.delete(0, tk.END)
    view_expenses()

def delete_expense():
    selected_item = expenses_tree.selection()
    if selected_item:
        item_text = expenses_tree.item(selected_item, "values")
        date,name,rent,need,transit,luxury,lent,savings = item_text
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
        with open("expenses.txt", "w") as file:
            for line in lines:
                if line.strip() != f"{date},{name},{rent},{need},{transit},{luxury},{lent},{savings}":
                    file.write(line)
        status_label.config(text="Expense deleted successfully!", fg="green")
        view_expenses()
    else:
        status_label.config(text="Please select an expense to delete!", fg="red")

def view_expenses():
    global expenses_tree
    if os.path.exists("expenses.txt"):
        total_expense = 0
        expenses_tree.delete(*expenses_tree.get_children())
        with open("expenses.txt", "r") as file:
            for line in file:
                date,name,rent,need,transit,luxury,lent,savings = line.strip().split(",")
                expenses_tree.insert("", tk.END, values=(date,name,rent,need,transit,luxury,lent,savings))
     #           print(rent,need,transit,luxury)
     #           print(type(rent),type(need),type(transit),type(luxury))
                #total_expense = total_expense+int(rent)+int(need)+int(transit)+int(luxury)
        total_label.config(text=f"Total Expense: {total_expense:.2f}")
    else:
        total_label.config(text="No expenses recorded.")
        expenses_tree.delete(*expenses_tree.get_children())

# Create the main application window
root = tk.Tk()
root.title("Expense Tracker")

# Create labels and entries for adding expenses
date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(row=1, column=0, padx=5, pady=5)
date_entry = tk.Entry(root)
#date_entry = datetime.datetime.now()
date_entry.grid(row=1, column=1, padx=5, pady=5)

name_label = tk.Label(root, text="Expense Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

rent_label = tk.Label(root, text="Rent:")
rent_label.grid(row=2, column=0, padx=5, pady=5)
rent_entry = tk.Entry(root, textvariable=tk.StringVar(value="0"))
rent_entry.grid(row=2, column=1, padx=5, pady=5)

need_label = tk.Label(root, text="Need:")
need_label.grid(row=3, column=0, padx=5, pady=5)
need_entry = tk.Entry(root, textvariable=tk.StringVar(value="0"))
need_entry.grid(row=3, column=1, padx=5, pady=5)

transit_label = tk.Label(root, text="Transit:")
transit_label.grid(row=4, column=0, padx=5, pady=5)
transit_entry = tk.Entry(root, textvariable=tk.StringVar(value="0"))
transit_entry.grid(row=4, column=1, padx=5, pady=5)

luxury_label = tk.Label(root, text="Luxury:")
luxury_label.grid(row=5, column=0, padx=5, pady=5)
luxury_entry = tk.Entry(root, textvariable=tk.StringVar(value="0"))
luxury_entry.grid(row=5, column=1, padx=5, pady=5)

lent_label = tk.Label(root, text="Lent:")
lent_label.grid(row=6, column=0, padx=5, pady=5)
lent_entry = tk.Entry(root, textvariable=tk.StringVar(value="0"))
lent_entry.grid(row=6, column=1, padx=5, pady=5)

savings_label = tk.Label(root, text="Savings:")
savings_label.grid(row=7, column=0, padx=5, pady=5)
savings_entry = tk.Entry(root, textvariable=tk.StringVar(value="0"))
savings_entry.grid(row=7, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10)

# Create a treeview to display expenses
columns = ("Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings")
expenses_tree = ttk.Treeview(root, columns=columns, show="headings")
expenses_tree.heading("Date", text="Date")
expenses_tree.heading("Name", text="Name")
expenses_tree.heading("Rent", text="Rent")
expenses_tree.heading("Need", text="Need")
expenses_tree.heading("Transit", text="Transit")
expenses_tree.heading("Luxury", text="Luxury")
expenses_tree.heading("Lent", text="Lent")
expenses_tree.heading("Savings", text="Savings")
expenses_tree.grid(row=9, column=0, columnspan=3, padx=5, pady=5)

# Create a label to display the total expense
total_label = tk.Label(root, text="")
total_label.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

# Create a label to show the status of expense addition and deletion
status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

# Create buttons to view and delete expenses
view_button = tk.Button(root, text="View Expenses", command=view_expenses)
view_button.grid(row=12, column=0, padx=5, pady=10)

delete_button = tk.Button(root, text="Delete Expense", command=delete_expense)
delete_button.grid(row=13, column=1, padx=5, pady=10)

# Check if the 'expenses.txt' file exists; create it if it doesn't
if not os.path.exists("expenses.txt"):
    with open("expenses.txt", "w"):
        pass

# Display existing expenses on application start
view_expenses()

root.mainloop()


with pd.ExcelWriter('excel_budget.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    existing_sheet.to_excel(writer, sheet_name=current_month, index=False, header=False, startrow=start_row)