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

n, l, s, u = 0,0,0,0
#password = list(password)

# checking strength
strength = ''
for i in password:
   if( i in numbers):
       n += 1
   if(i in lowerCase):
       l += 1
   if(i in specialChars):
       s += 1
   if(i in upperCase):
       u += 1

if(n>=1 and l>=1 and s>=1 and u>=1):
   print("Password Strength: Very Strong") 
elif(n>=1 and l>=1 and s>=1):
   print("Password Strength: Strong") 
elif(n>=1 and l>=1):
   print("Password Strength: Medium") 
elif(n>=1):
   print("Password Strength: Low") 
else: 
   print("Password Strength: Not secure")

         
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


