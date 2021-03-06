

import os
import sys
import csv
import re

# ahoj

print('Vítej v kuchařce', os.getlogin())


#input uživatele jméno a příjmení jestli uživatel zadá správně vypsat hlášku jestliže nezadá aspon písmeno ukončí se program
jmeno = input("Zadej jméno: ")
re.search('[a-zA-Z]', jmeno)

if (re.search('[a-zA-Z]', jmeno)):
  print("Můžete pokračovat zadáním příjmení")
else: print("špatně")

prijmeni = input("Zadej příjmení: ")
print(prijmeni)
kontrola1 = re.search('[a-zA-Z]', prijmeni,)
if (re.search('[a-zA-Z]', prijmeni)):
  print("Jméno a příjmení bylo zadáno správně")
else: print("špatně")












#val = input("Enter your value: ")
#print(val)


