#HLAVIČKA
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Linhart
email: michal.linhy@seznam.cz
discord: Michal.L
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registrovani_uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"} #registrovaní uživatelé ze zadání v podobě dict knihovny
cara = "-" * 40
username = input("username:")   #uživatelské jméno
password = input("password:")   #heslo

#PŘIHLÁŠENÍ
if registrovani_uzivatele.get(username) != password:    #podmínka, pokud se jméno a heslo neshodují pomocí klíče a hodnoty z "registrovaní uživatelé"
    print("unregistered user, terminating the program..")

else:
    print(cara)     #pokud se shodují
    print(f"""Welcome to the app, {username}
We have {len(TEXTS)} texts to be analyzed""")
    print(cara)
    
    #VÝBĚR TEXTU
    cislo_textu = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")     #pokud projde přes přihlášení, vybere číslo textu podle indexu z "TEXTS"
    
    if not cislo_textu.isdigit() or not (1 <= int(cislo_textu) <= len(TEXTS)):  #pokud vybere jiné čislo, než je od 1 do 3, ukončí program
        print("Invalid selection, terminating the program.. ")

    else:
        zvoleny_text = TEXTS[int(cislo_textu) - 1]
        slova = zvoleny_text.split()    #rozdělení textu na jednotlivá slova

        #POČTY
        pocet_slov = len(slova)
        
        pocet_titlecase = 0     #počet slov začínajících velkým písmenem
        pocet_uppercase = 0     #počet slov psaných velkými písmeny
        pocet_lowercase = 0     #počet slov psaných malými písmeny
        pocet_numeric = 0       #počet slov, která jsou číslice
        soucet_numeric = 0      #součet hodnoty číslic
       
        for slovo in slova:
            slovo = slovo.strip(",.?!")  # očištění od znaků

            if slovo.istitle():
                pocet_titlecase += 1
            
            elif slovo.isupper():
                pocet_uppercase += 1
            
            elif slovo.islower():
                pocet_lowercase += 1

            if slovo.isdigit():  # součet čísel a jejich počet
                pocet_numeric += 1
                soucet_numeric += int(slovo)  # převod slova na číslo
               

        print("There are", pocet_slov, "words in the selected text.")   
        print("There are", pocet_titlecase, "titlecase words." )    
        print("There are", pocet_uppercase, "uppercase words.")
        print("There are", pocet_lowercase, "lowercase words.")
        print("There are", pocet_numeric, "numeric strings.")
        print("The sum of all the numbers", soucet_numeric)
        print(cara)

        #GRAF
        delky_slov = {} #prázdný set
        for slovo in slova:
            ocistene_slovo = slovo.strip(",.?!")    #očištění od znaků
            delka = len(ocistene_slovo)     #délka očištěného slova
            if delka in delky_slov:
                delky_slov[delka] += 1
            else:
                delky_slov[delka] = 1

        print("LEN|     OCCURENCES     |NR.")    #hlavička grafu
        print("----------------------------------------")   #čára
        for delka in sorted(delky_slov):    #seřazení 
            print(f"{delka:3}| {'*' * delky_slov[delka]:18} |{delky_slov[delka]}")


            