import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from datetime import datetime

# File name to save the data
FILE_NAME = "yearly_budget.xlsx"

# Thresholds for suggestions
THRESHOLDS = {
    "Rent": 8000,
    "Transit": 3000,
    "Essentials": 2000,
    "Luxury": 8000,
    "Market Investment": 3000,
}

# Get the current month name
current_month = datetime.now().strftime("%B")

# Save data to the file with monthly sheets
def save_to_file(data):
    if os.path.exists(FILE_NAME):
        # Load the existing file
        with pd.ExcelWriter(FILE_NAME, mode="a", if_sheet_exists="overlay") as writer:
            try:
                # Read existing sheet for the current month
                existing_data = pd.read_excel(FILE_NAME, sheet_name=current_month)
                existing_data = pd.concat([existing_data, pd.DataFrame([data])], ignore_index=True)
            except ValueError:
                # If the sheet for the current month doesn't exist, create a new one
                existing_data = pd.DataFrame([data])
            
            # Save the data to the sheet
            existing_data.to_excel(writer, sheet_name=current_month, index=False)
    else:
        # Create a new Excel file with the current month sheet
        with pd.ExcelWriter(FILE_NAME) as writer:
            pd.DataFrame([data]).to_excel(writer, sheet_name=current_month, index=False)

    messagebox.showinfo("Success", f"Data saved to {FILE_NAME} under {current_month} sheet.")

# Check for suggestions based on thresholds
def check_suggestions(data):
    warnings = []
    if data["Category"] == "Expenditures":
        for key, value in data.items():
            if key in THRESHOLDS and value > THRESHOLDS[key]:
                warnings.append(f"{key} exceeds the threshold of {THRESHOLDS[key]}.")
    elif data["Category"] == "Savings" and "Market" in data:
        if data["Market"] > THRESHOLDS["Market Investment"]:
            warnings.append("Market investment is high. Consider the risks before proceeding.")

    if warnings:
        messagebox.showwarning("Warning", "\n".join(warnings))

# Handle category selection
def select_category():
    category = category_var.get()
    if category == "Expenditures":
        show_expenditures()
    elif category == "Income":
        show_income()
    elif category == "Savings":
        show_savings()
    else:
        messagebox.showerror("Error", "Please select a valid category.")

# Show expenditures input form
def show_expenditures():
    clear_frame()
    tk.Label(root, text="Enter Expenditures").grid(row=0, column=0, columnspan=2)

    tk.Label(root, text="Rent:").grid(row=1, column=0)
    rent_entry.grid(row=1, column=1)

    tk.Label(root, text="Transit:").grid(row=2, column=0)
    transit_entry.grid(row=2, column=1)

    tk.Label(root, text="Essentials:").grid(row=3, column=0)
    essentials_entry.grid(row=3, column=1)

    tk.Label(root, text="Luxury:").grid(row=4, column=0)
    luxury_entry.grid(row=4, column=1)

    tk.Button(root, text="Save", command=save_expenditures).grid(row=5, column=0, columnspan=2)

# Save expenditures
def save_expenditures():
    data = {
        "Category": "Expenditures",
        "Rent": float(rent_entry.get() or 0),
        "Transit": float(transit_entry.get() or 0),
        "Essentials": float(essentials_entry.get() or 0),
        "Luxury": float(luxury_entry.get() or 0),
    }
    check_suggestions(data)
    save_to_file(data)
    clear_frame()
    show_main_menu()

# Show income input form
def show_income():
    clear_frame()
    tk.Label(root, text="Enter Income").grid(row=0, column=0, columnspan=2)

    tk.Label(root, text="Salary:").grid(row=1, column=0)
    salary_entry.grid(row=1, column=1)

    tk.Label(root, text="Other Income:").grid(row=2, column=0)
    other_income_entry.grid(row=2, column=1)

    tk.Button(root, text="Save", command=save_income).grid(row=3, column=0, columnspan=2)

# Save income
def save_income():
    data = {
        "Category": "Income",
        "Salary": float(salary_entry.get() or 0),
        "Other Income": float(other_income_entry.get() or 0),
    }
    save_to_file(data)
    clear_frame()
    show_main_menu()

# Show savings input form
def show_savings():
    clear_frame()
    tk.Label(root, text="Enter Savings").grid(row=0, column=0, columnspan=2)

    tk.Label(root, text="Chits:").grid(row=1, column=0)
    chits_entry.grid(row=1, column=1)

    tk.Label(root, text="Market:").grid(row=2, column=0)
    market_entry.grid(row=2, column=1)

    tk.Label(root, text="Other Savings:").grid(row=3, column=0)
    other_savings_entry.grid(row=3, column=1)

    tk.Button(root, text="Save", command=save_savings).grid(row=4, column=0, columnspan=2)

# Save savings
def save_savings():
    data = {
        "Category": "Savings",
        "Chits": float(chits_entry.get() or 0),
        "Market": float(market_entry.get() or 0),
        "Other Savings": float(other_savings_entry.get() or 0),
    }
    check_suggestions(data)
    save_to_file(data)
    clear_frame()
    show_main_menu()

# Clear the frame
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

# Show the main menu
def show_main_menu():
    tk.Label(root, text="Daily Budget Tracker", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

    tk.Label(root, text="Select a category to update:").grid(row=1, column=0, columnspan=2)

    tk.Radiobutton(root, text="Expenditures", variable=category_var, value="Expenditures").grid(row=2, column=0)
    tk.Radiobutton(root, text="Income", variable=category_var, value="Income").grid(row=2, column=1)
    tk.Radiobutton(root, text="Savings", variable=category_var, value="Savings").grid(row=3, column=0)

    tk.Button(root, text="Next", command=select_category).grid(row=4, column=0, columnspan=2)

# Initialize the main window
root = tk.Tk()
root.title("Yearly Budget Tracker")

# Variables
category_var = tk.StringVar(value="")

rent_entry = tk.Entry(root)
transit_entry = tk.Entry(root)
essentials_entry = tk.Entry(root)
luxury_entry = tk.Entry(root)

salary_entry = tk.Entry(root)
other_income_entry = tk.Entry(root)

chits_entry = tk.Entry(root)
market_entry = tk.Entry(root)
other_savings_entry = tk.Entry(root)

# Start the app
show_main_menu()
root.mainloop()
