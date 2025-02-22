import os
import datetime
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for
import base64
from io import BytesIO
from openpyxl import load_workbook

app = Flask(__name__)

# Excel file for local storage
excel_file = "expenses.xlsx"

def get_month_name(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%d-%b").strftime("%B")
    except ValueError:
        return datetime.datetime.now().strftime("%B")

def load_data(sheet_name):
    if os.path.exists(excel_file):
        with pd.ExcelFile(excel_file, engine="openpyxl") as xls:
            if sheet_name in xls.sheet_names:
                return pd.read_excel(xls, sheet_name=sheet_name, engine="openpyxl")
    return pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"])

def save_data(data, sheet_name):
    with pd.ExcelWriter(excel_file, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
        data.to_excel(writer, sheet_name=sheet_name, index=False)

def generate_chart(data):
    categories = ["Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]
    values = [data[col].astype(float).sum() for col in categories]
    
    print(f"Chart Data: {values}")  # Debugging: Check values being passed
    
    if sum(values) == 0:
        print("No expenses to plot.")  # Debugging
        return None
    
    fig, ax = plt.subplots(figsize=(5, 3), facecolor='#121212')
    ax.pie(values, labels=categories, autopct="%1.1f%%", startangle=90, 
           colors=["#ff4444", "#448aff", "#00e676", "#ffbb33", "#aa66cc", "#ff80ab"],
           textprops={'color': 'white'})
    ax.set_title("Expense Distribution", color='white')
    
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight', facecolor='#121212')
    buf.seek(0)
    plt.close(fig)  # Free memory
    
    return base64.b64encode(buf.getvalue()).decode("utf-8")

@app.route('/')
def index():
    current_month = datetime.datetime.now().strftime("%B")
    data = load_data(current_month)
    summary = {col: data[col].astype(float).sum() for col in ["Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]} if not data.empty else {}
    chart = generate_chart(data)
    return render_template("index.html", data=data.to_dict(orient='records'), summary=summary, chart=chart)

@app.route('/add', methods=['POST'])
def add_expense():
    date_str = request.form.get("date") or datetime.datetime.now().strftime("%d-%b")
    month_name = get_month_name(date_str)
    
    data = load_data(month_name)
    new_row = pd.DataFrame([{ 
        "Date": date_str,
        "Name": request.form.get("name") or " ",
        "Rent": request.form.get("rent") or "0",
        "Need": request.form.get("need") or "0",
        "Transit": request.form.get("transit") or "0",
        "Luxury": request.form.get("luxury") or "0",
        "Lent": request.form.get("lent") or "0",
        "Savings": request.form.get("savings") or "0"
    }])
    data = pd.concat([data, new_row], ignore_index=True)
    save_data(data, month_name)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

