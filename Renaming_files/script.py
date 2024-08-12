'''*********************************************************************************************************************************
 * Name                 : script.py
 * Creation Date        : 25-05-2022
 * Last Modified        : 06-06-2022
----------------------------------------------------------------------------------------------------------------------------------
 * Author               : Badam Mayur Krishna
 * Author's Email       : mayurkrishna.b@alpha-numero.tech
----------------------------------------------------------------------------------------------------------------------------------
* Description           : Renaming files by taking strings in an xlsx file with strings from another xlsx. 
**********************************************************************************************************************************'''

#import os library for renaming files
import os

#opening files which have the names
file_to_be_renamed_list = open(r"/home/mayurkrishna.b/svn/mayurkrishna/Assignments/Python/pa_8/file_to_be_renamed_list.txt","r+")

renamed_file_list = open(r"/home/mayurkrishna.b/svn/mayurkrishna/Assignments/Python/pa_8/renamed_file_list.txt","r+")

#print(type(to_be_renamed_list)) 
#print(to_be_renamed_list) 

#Writing the names into a list by reading the excels
to_be_renamed_list = file_to_be_renamed_list.read().splitlines()
rename_file_list = renamed_file_list.read().splitlines()

#A = ["mika.csv \n", "xyz.txt \n", "qwerty.xlsx \n", "utiamc.sv \n"]
#B = ["milkha.csv \n", "abc.txt \n", "asdfg.xlsx \n", "namamc.sv \n"]

#file_to_be_renamed_list.writelines(A)
#print(to_be_renamed_list)


#print(type(to_be_renamed_list[1])) 
#print(to_be_renamed_list)

#Renaming files
for x in range(0,4):
   os.rename(to_be_renamed_list[x], rename_file_list[x])
