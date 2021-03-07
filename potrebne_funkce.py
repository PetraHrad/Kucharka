import os
import sys
import csv
import re


def kontrola_pismen():
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


def kontrola_veku():
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
        quit()


def kontrola_emailu():
    email = input("Zadej svůj email:")
    if email.__contains__('@') and email.__contains__('.'):
        print("Email je v pořádku. Můžete pokračovat dál")
    else:
        print("Email není správný. Konec programu.")
        quit()