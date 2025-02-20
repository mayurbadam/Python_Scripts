import os
import tkinter as tk
from tkinter import ttk
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Get current month
current_month = datetime.datetime.now().strftime("%m")

# Load existing data from Excel if available
excel_file = "excel_budget.xlsx"
def load_data():
    try:
        return pd.read_excel(excel_file, sheet_name=current_month, engine="openpyxl")
    except (FileNotFoundError, ValueError):
        return pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"])
existing_sheet = load_data()

def add_expense():
    global existing_sheet
    date = date_entry.get() or datetime.datetime.now().strftime("%d-%b")
    name = name_entry.get() or " "
    rent = rent_entry.get() or "0"
    need = need_entry.get() or "0"
    transit = transit_entry.get() or "0"
    luxury = luxury_entry.get() or "0"
    lent = lent_entry.get() or "0"
    savings = savings_entry.get() or "0"

    new_row = pd.DataFrame([{ "Date": date, "Name": name, "Rent": rent, "Need": need, "Transit": transit, "Luxury": luxury, "Lent": lent, "Savings": savings }])
    existing_sheet = pd.concat([load_data(), new_row], ignore_index=True)
    
    with pd.ExcelWriter(excel_file, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        existing_sheet.to_excel(writer, sheet_name=current_month, index=False)
    
    status_label.config(text="Expense added successfully!", fg="green")
    clear_expenses()
    view_expenses()

def view_expenses():
    expenses_tree.delete(*expenses_tree.get_children())
    for _, row in load_data().iterrows():
        expenses_tree.insert("", tk.END, values=row.tolist())
    show_summary()
    plot_expenses()

def clear_expenses():
    date_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    for entry in entries.values():
        entry.delete(0, tk.END)
        entry.insert(0, "0")

def show_summary():
    data = load_data()
    summary_text = "Summary:\n"
    if not data.empty:
        for col in ["Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]:
            summary_text += f"{col}: {data[col].astype(float).sum():.2f}\n"
    summary_label.config(text=summary_text)

def plot_expenses():
    data = load_data()
    if data.empty:
        return
    fig, ax = plt.subplots(figsize=(4, 3))
    categories = ["Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]
    values = [data[col].astype(float).sum() for col in categories]
    ax.pie(values, labels=categories, autopct="%1.1f%%", startangle=90, colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"])
    ax.set_title("Expense Distribution")
    
    for widget in chart_frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x400")

frame_top = tk.Frame(root)
frame_top.pack(fill="x", padx=5, pady=5)

frame_bottom = tk.Frame(root)
frame_bottom.pack(fill="both", expand=True, padx=5, pady=5)

frame_left = tk.Frame(frame_bottom)
frame_left.pack(side="left", padx=5, pady=5)

tk.Label(frame_top, text="Date (DD-MMM):").pack(side="left")
date_entry = tk.Entry(frame_top, width=10)
date_entry.pack(side="left", padx=5)
tk.Label(frame_top, text="Expense Name:").pack(side="left")
name_entry = tk.Entry(frame_top, width=15)
name_entry.pack(side="left", padx=5)

tk.Label(frame_left, text="Categories:").pack()
categories = ["Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]
entries = {}
for category in categories:
    frame = tk.Frame(frame_left)
    frame.pack(fill="x")
    tk.Label(frame, text=f"{category}:", width=8, anchor="w").pack(side="left")
    entry = tk.Entry(frame, width=8)
    entry.insert(0, "0")
    entry.pack(side="left")
    entries[category.lower()] = entry

rent_entry, need_entry, transit_entry, luxury_entry, lent_entry, savings_entry = [entries[cat.lower()] for cat in categories]

tk.Button(frame_left, text="Add Expense", command=add_expense).pack(pady=5)

columns = ("Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings")
expenses_tree = ttk.Treeview(frame_left, columns=columns, show="headings", height=5)
for col in columns:
    expenses_tree.heading(col, text=col)
    expenses_tree.column(col, width=60)  # Adjusting column width
expenses_tree.pack()

status_label = tk.Label(frame_left, text="", fg="green")
status_label.pack()

tk.Button(frame_left, text="View Expenses", command=view_expenses).pack(pady=5)

if not os.path.exists(excel_file):
    with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
        pd.DataFrame(columns=columns).to_excel(writer, sheet_name=current_month, index=False)

summary_label = tk.Label(frame_left, text="", justify="left")
summary_label.pack()

chart_frame = tk.Frame(frame_left)
chart_frame.pack()

view_expenses()
root.mainloop()