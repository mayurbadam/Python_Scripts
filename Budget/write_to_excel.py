import pandas as pd

# Replace "existing_sheet.xlsx" with the name of your existing Excel sheet
existing_sheet = pd.read_excel("excel_budget.xlsx")

# Replace "new_data.csv" with the name of your new data file
#new_data = pd.read_csv("new_data.csv")
 
print(existing_sheet)

with pd.ExcelWriter('excel_budget.xlsx', engine='openpyxl', mode='a') as writer:
    new_df.to_excel(writer, sheet_name='Sheet2', index=False, header=None)
