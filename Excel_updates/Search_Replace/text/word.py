'''*********************************************************************************************************************************
 * Name                 : script.py
 * Creation Date        : 25-05-2022
 * Last Modified        : 06-06-2022
----------------------------------------------------------------------------------------------------------------------------------
 * Author               : Badam Mayur Krishna
 * Author's Email       : mayurkrishna.b@alpha-numero.tech
----------------------------------------------------------------------------------------------------------------------------------
* Description           : Searching and replacing single or multi word pattern in a text file
**********************************************************************************************************************************'''

import os
import sys
import fileinput

#taking input for the string to be searched.
print ("Text to search for:")
textToSearch = input( "> " )

#taking input for the string to be replaced.
print ("Text to replace it with:")
textToReplace = input( "> " )

#taking input for the file to make changes 
print ("File to perform Search-Replace on:")
fileToSearch  = input( "> " )

#opening file in read and write mode
tempFile = open( fileToSearch, 'r+' )

#searching for the string in every line and writing into the file
for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
        print('Match Found')
    else:
        print('Match Not Found!!')
    tempFile.write( line.replace( textToSearch, textToReplace ) )
tempFile.close()

input( '\n\n Press Enter to exit...' )
