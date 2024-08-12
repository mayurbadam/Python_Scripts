'''*********************************************************************************************************************************
 * Name                 : a.py
 * Creation Date        : 25-05-2022
 * Last Modified        : 06-06-2022
----------------------------------------------------------------------------------------------------------------------------------
 * Author               : Badam Mayur Krishna
 * Author's Email       : mayurkrishna.b@alpha-numero.tech
----------------------------------------------------------------------------------------------------------------------------------
* Description           : 
   Program for checking the password strength 
   Password should contain:
   numbers --> strength = Low
   numbers, alphabets --> strength = Medium 
   numbers, alphabets,symbols --> strength = Strong
   numbers, alphabets,symbols, atleast one uppercase alphabet --> strength = Very Strong
**********************************************************************************************************************************'''
#importing required modules
import random
import string
import array
import itertools

password = input("Enter password: ")

#Data for comparing
numbers = list(string.digits)
lowerCase = list(string.ascii_lowercase)
upperCase = list(string.ascii_uppercase)
specialChars = list("!~`@#$%^&*()_+{}:|?>/.<,;\"")

#password = list(password)

# checking strength
strength = ''
for i in password:
   for j in numbers:
      if i==j:
         strength = 'Low'
         break
if(strength == 'Low'):
   for i in password:
      for j in lowerCase:
         if i==j:
            strength = 'Medium'
            break
if(strength == 'Medium'):
   for i in password:
      for j in specialChars:
         if i==j:
            strength = 'Strong'
            break
if(strength == 'Strong'):
   for i in password:
      for j in upperCase:
         if i==j:
            strength = 'Very Strong'
            break
else: 
   strength = 'Not secure'
print("Password Strength: " + strength)

         
#OUTPUTS:
# Enter password: 38279289
# Password Strength: Low
# 
# Enter password: 1232awsrdas
# Password Strength: Medium
# 
# Enter password: qwe123#44$
# Password Strength: Strong
# 
# Enter password: ASsdfds123#$#@
# Password Strength: Very Strong
