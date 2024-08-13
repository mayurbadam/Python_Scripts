'''*********************************************************************************************************************************
 * Name                 : script.py
 * Creation Date        : 25-05-2022
 * Last Modified        : 06-06-2022
----------------------------------------------------------------------------------------------------------------------------------
 * Author               : Badam Mayur Krishna
 * Author's Email       : mayurkrishna.b@alpha-numero.tech
----------------------------------------------------------------------------------------------------------------------------------
* Description           : Search and replace single line or multiline string, containing special characters in a text file
**********************************************************************************************************************************'''

import os
import sys
import fileinput

#taking input for the no.of lines to be searched.
print ("No.of lines: ")
no_of_lines = int(input( "> " ))

#taking input for the string to be searched.
print ("Text to search for:")

#setting an empty string to set the data type
textToSearch = ''''''
for i in range(no_of_lines):
    textToSearch+=input("> ")+"\n"
print(textToSearch)

#taking input for the string to be replaced.
print ("Text to replace it with:")

textToReplace = ''''''
for i in range(no_of_lines):
    textToReplace+=input("> ")+"\n"
print(textToReplace)

#taking input for the file to make changes 
print ("File to perform Search-Replace on:")
fileToSearch  = input( "> " )
print(fileToSearch)

#opening the file to read from the file and storing into a string and then closing the file
totalText= ''''''
with open(fileToSearch, 'r') as file1:
   totalText = file1.read()
file1.close()

#print(totalText)

#replacing the text
totalText = totalText.replace(textToSearch, textToReplace)
print('Match Found')

#opening the file to write into the file and from the replaced string and then closing the file
with open(fileToSearch, 'w') as file1:
   file1.write(totalText)
file1.close()

input('\n\n Press Enter to exit...')
