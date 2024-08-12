'''*********************************************************************************************************************************
 * Name                 : a.py
 * Creation Date        : 25-05-2022
 * Last Modified        : 06-06-2022
----------------------------------------------------------------------------------------------------------------------------------
 * Author               : Badam Mayur Krishna
 * Author's Email       : mayurkrishna.b@alpha-numero.tech
----------------------------------------------------------------------------------------------------------------------------------
* Description           : Script for password generation according to user following needs. Numbers + special characters
**********************************************************************************************************************************'''
#importing random for generating random values
import random
#string module for performing various string operations
import string
#array module for using arrays
import array

#############################################################################
# Script for password generation according to user following needs. Numbers #
#############################################################################
password = random.randint(0 , 99999999)

print("Password with only Numbers :  " + str(password))

##################################################################################################
# Script for password generation according to user following needs. Numbers + special characters #
##################################################################################################
#Lists which act like libraries for numbers, special characters
numbers = list(string.digits)
special_chars = list("!@#$%^&*()_+{}:<>?")

totalList = numbers + special_chars

#print(numbers)
#print(special_chars)
#print(totalList)

#generating random values
randNumber = random.choice(numbers)
randSpecial = random.choice(special_chars)

temp = randNumber + randSpecial

for x in range(10):
	temp = temp + random.choice(totalList)

tempList = array.array('u',temp)
random.shuffle(tempList)

password = ''

for x in tempList:
	password = password + x

print("Password with Numbers,Special characters:  " + str(password))

###########################################################################
## Script for password generation according to user following needs.     ##
##    Number + Special Characters + Small case and Upper-Case characters ##
###########################################################################
numbers = list(string.digits)
lowerCase = list(string.ascii_lowercase)
upperCase = list(string.ascii_uppercase)
specialChars = list("!@#$%^&*()_+{}:<>?")

totalList = numbers + specialChars + lowerCase + upperCase

#print(numbers)
#print(special_chars)
#print(totalList)

randNumber = random.choice(numbers)
randSpecial = random.choice(specialChars)
randLow = random.choice(lowerCase)
randUp = random.choice(upperCase)

temp = randNumber + randSpecial + randLow + randUp

for x in range(8):
	temp = temp + random.choice(totalList)

tempList = array.array('u',temp)
random.shuffle(tempList)

password = ''

for x in tempList:
	password = password + x

print("Password with Numbers,Special Characters,Small-case and Upper-Case characters:  " + str(password))
