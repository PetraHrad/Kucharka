

import os
import sys
import csv
import re

# ahoj

print('Vítej v kuchařce', os.getlogin())

# input uživatele jméno a příjmení jestli uživatel zadá správně vypsat hlášku
# jestliže nezadá aspon písmeno ukončí se program


def kotrola_pismen():
  while True:
    jmeno = input("Zadej jméno: ")
    if jmeno.isalpha():
        print("Můžete pokračovat zadáním příjmení")
        break
    else:
        print("Jméno obsahuje číslice/znaky, prosím o zadání jména bez číslic/znaky: ")
        continue
  while True:
    prijmeni = input("Zadej příjmení: ")
    if prijmeni.isalpha():
        print("Můžete pokračovat zadáním věku")
        break
    else:
        print("Příjmení obsahuje číslice/znaky, prosím o zadání příjmení bez číslic/znaky: ")
        continue


while True:
    try:
        vek = int(input("Prosím zadejte svůj věk: "))
    except ValueError:
        print("Prosím o zadání znovu:")
        continue
    else:
        break
if vek >= 12:
    print("Můžete pokračovat dále")
else:
    print("Omlouváme se, ale tyto informace jsou dostupné jen pro starší 12let")














#val = input("Enter your value: ")
#print(val)


