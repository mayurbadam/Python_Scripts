#Importing the CSV module
import csv
import sys

new = sys.argv[1] if len(sys.argv) >=2 else "0"

# Opening the file in append mode.
with open('tracking_sheet.csv', 'a', newline="") as file:
   myFile = csv.writer(file)
#print("file opened")

# Writing the column headers  
   if new == 1:
      myFile.writerow(["Task","Start Date","Start Date time","End Data","End Date Time","Total Time", "Priority","Task size","Task Lable","Task complexity","Status"])

# Getting the number of rows to add  
   total_task = int(input("Enter no.of tasks: "))

# Using for loop to write user input to the file  
   for i in range(total_task):
        task = input("Task "+ str(i+1) +": Enter Task: ")
        start_date = input("Task "+ str(i+1) +": Enter Start Date: ")
        start_date_t = input("Task "+ str(i+1) +": Enter Start Date time: ")
        end_data = input("Task "+ str(i+1) +": Enter End Date: ")
        end_data_t = input("Task "+ str(i+1) +": Enter End Date time: ")
        total_t = input("Task "+ str(i+1) +": Enter Total time: ")
        priority = input("Task "+ str(i+1) +": Enter Priority: ")
        task_size = input("Task "+ str(i+1) +": Enter Task size: ")
        task_lable = input("Task "+ str(i+1) +": Task Lable: ")
        complexity = input("Task "+ str(i+1) +": Enter Complexity: ")
        status = input("Task "+ str(i+1) +": Enter Status: ")
        myFile.writerow([task,start_date,start_date_t,end_data,end_data_t,total_t,priority,task_size,task_lable,complexity,status])
   print("Writing done")
