import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for
import base64
from io import BytesIO
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("google_sheets_credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("ExpenseTracker").sheet1

# Load existing data from Google Sheets
def load_data():
    data = sheet.get_all_records()
    return pd.DataFrame(data) if data else pd.DataFrame(columns=["Date", "Name", "Rent", "Need", "Transit", "Luxury", "Lent", "Savings"])

# Generate expense distribution chart
def generate_chart(data):
    if data.empty:
        return None
    categories = ["Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]
    values = [data[col].astype(float).sum() for col in categories]
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.pie(values, labels=categories, autopct="%1.1f%%", startangle=90, colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"])
    ax.set_title("Expense Distribution")
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

@app.route('/')
def index():
    data = load_data()
    summary = {col: data[col].astype(float).sum() for col in ["Rent", "Need", "Transit", "Luxury", "Lent", "Savings"]} if not data.empty else {}
    chart = generate_chart(data)
    return render_template("index.html", data=data.to_dict(orient='records'), summary=summary, chart=chart)

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

    new_row = [date, name, rent, need, transit, luxury, lent, savings]
    sheet.append_row(new_row)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

