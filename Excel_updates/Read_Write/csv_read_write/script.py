'''*********************************************************************************************************************************
 * Name                 : script.py
 * Creation Date        : 25-05-2022
 * Last Modified        : 06-06-2022
----------------------------------------------------------------------------------------------------------------------------------
 * Author               : Badam Mayur Krishna
 * Author's Email       : mayurkrishna.b@alpha-numero.tech
----------------------------------------------------------------------------------------------------------------------------------
* Description           : Reading and writing to following file types - CSV file
**********************************************************************************************************************************'''

import csv

#defining lists for writing into list
fields = ["Name","location","Emp.no"]
rows = [['Mayur','HYD', 'AN215'],['xyz1', 'AHM', 'AN111'],['xyz2', 'HYD','AN321'],['xyz3','AHM','AN123']]

#specifying the file to access
filename = "a.csv"

#opening file in write mode
with open(filename, 'w') as csvfile:
   #using writer method in csv to write
   csvwriter = csv.writer(csvfile)
   csvwriter.writerow(fields)
   csvwriter.writerows(rows)

#opening file in read mode
with open(filename,'r') as csvfile:
   #using reader method in csv to write
   csvreader = csv.reader(csvfile)
   fields = next(csvreader)

   for row in csvreader:
      rows.append(row)

   print("Total no.of rows: %d"%(csvreader.line_num))

flist = " ".join(fields)

#printing the list read
print(flist)

#printing the rows read
for row in range(0,4):
   rowl = rows[row]
   #for col in range(len(rowl)-2):
   rowls = " ".join(rowl)
   print(rowls)

#OUTPUT:
# Total no.of rows: 5
# Name location Emp.no
# Mayur HYD AN215
# xyz1 AHM AN111
# xyz2 HYD AN321
# xyz3 AHM AN123






#for reference - old code
#Reading from excel
#import openpyxl
#book = openpyxl.load_workbook('a.xlsx')
#
#sheet = book.active
#
#a1 = sheet['C9']
#a2 = sheet['B9']
#a3 = sheet.cell(row=9, column=2)
#
#print(a1.value)
#print(a2.value) 
#print(a3.value)
#
#print(type(book))
#print(book)
#



#for row in rows:
#   x=0
#   rlist = " ".join(rows[x])
#   x = x+1


