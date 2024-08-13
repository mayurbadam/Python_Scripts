'''*********************************************************************************************************************************
 * Name                 : script.py
 * Creation Date        : 25-05-2022
 * Last Modified        : 06-06-2022
----------------------------------------------------------------------------------------------------------------------------------
 * Author               : Badam Mayur Krishna
 * Author's Email       : mayurkrishna.b@alpha-numero.tech
----------------------------------------------------------------------------------------------------------------------------------
* Description           : Reading and writing to following file types - Text file
**********************************************************************************************************************************'''

# writing data in a file.
file1 = open("myfile.txt","w")

#defining list to write data into cells in excel
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
  
#writing using different methods
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes

#Opening text file in read mode 
file1 = open("myfile.txt","r+") 
  
print("Output of Read function is ")
print(file1.read())
print()
  
# seek(n) takes the file handle to the nth bite from the beginning.
file1.seek(0) 
  
print( "Output of Readline function is ")
print(file1.readline()) 
print()
  
file1.seek(0)
  
# To show difference between read and readline
print("Output of Read(9) function is ") 
print(file1.read(9))
print()
  
file1.seek(0)
  
print("Output of Readline(9) function is ") 
print(file1.readline(9))
  
file1.seek(0)
# readlines function
print("Output of Readlines function is ") 
print(file1.readlines()) 
print()
file1.close()
