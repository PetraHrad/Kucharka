
from potrebne_funkce import *
from soubor_recepty import recepty
import os



# ahoj

print('Vítej v kuchařce', os.getlogin())

kontrola_pismen()
kontrola_veku()
kontrola_emailu()


def prochazeni_kucharky():
    list_receptu = []
    list_nazev_receptu = []
    print("Pro zobrazení receptu zvolte z následujících možností")
    x = 1
    for item in recepty:
        print(f'{x}. ' + item)
        list_receptu.append(x)
        list_nazev_receptu.append(item)
        x = x + 1
    print()
    while True:
        vyber = int(input(f'Prosím vyberte ({min(list_receptu)} - {max(list_receptu)}):'))
        if vyber > max(list_receptu) or vyber < min(list_receptu):
            print("Vybrané číslo receptu neexistuje")
            continue
        else:
            print(f"Váš výběr je recept číslo {vyber}.Děkuji")
            vyber -= 1
            return str(recepty[list_nazev_receptu[vyber]])


recept = prochazeni_kucharky()
print(recept)


def zapis_do_worpad(in_recept):
    with open("recept.txt", "a") as myFile:
        myFile.write("\n" + in_recept)
        myFile.close()


zapis_do_worpad(recept)






