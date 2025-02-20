import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Get current month
current_month = datetime.datetime.now().strftime("%m")

# Load existing data from Excel if available
excel_file = "excel_budget.xlsx"
def load_data():
    try:
        return pd.read_excel(excel_file, sheet_name=current_month, engine="openpyxl")
    except (FileNotFoundError, ValueError):
        return pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"])

@app.route('/')
def index():
    data = load_data()
    summary = {col: data[col].astype(float).sum() for col in ["Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]} if not data.empty else {}
    return render_template("index.html", data=data.to_dict(orient='records'), summary=summary)

@app.route('/add', methods=['POST'])
def add_expense():
    date = request.form.get("date") or datetime.datetime.now().strftime("%d-%b")
    name = request.form.get("name") or " "
    rent = request.form.get("rent") or "0"
    need = request.form.get("need") or "0"
    transit = request.form.get("transit") or "0"
    luxury = request.form.get("luxury") or "0"
    lent = request.form.get("lent") or "0"
    savings = request.form.get("savings") or "0"

    new_row = pd.DataFrame([{ "Date": date, "Name": name, "Rent": rent, "Need": need, "Transit": transit, "Luxury": luxury, "Lent": lent, "Savings": savings }])
    existing_data = load_data()
    updated_data = pd.concat([existing_data, new_row], ignore_index=True)
    
    with pd.ExcelWriter(excel_file, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        updated_data.to_excel(writer, sheet_name=current_month, index=False)
    
    return redirect(url_for("index"))

if __name__ == "__main__":
    if not os.path.exists(excel_file):
        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]).to_excel(writer, sheet_name=current_month, index=False)
    app.run(debug=True)