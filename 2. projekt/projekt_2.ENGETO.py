"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michal Linhart
email: michal.linhy@seznam.cz
discord: Michal L.
"""

import random
import time

cara = "-" * 47

def generuj_tajne_cislo():
    """Vygeneruje tajné 4místné číslo s unikátními číslicemi, nezačínající nulou."""
    cisla = []
    
    # První číslice, která nesmí být nula
    cisla.append(random.randint(1, 9))
    
    # Zbytek tří číslic
    while len(cisla) < 4:
        nove_cislo = random.randint(0, 9)
        if nove_cislo not in cisla:
            cisla.append(nove_cislo)
    
    # Převod číslic na řetězec
    tajne_cislo = ''.join(str(cislo) for cislo in cisla)
    return tajne_cislo

#HÁDÁNÍ
def vyhodnot_hadani(tajne_cislo, hadani):
    """Vyhodnotí uživatelský tip a vrátí počet bulls a cows."""
    bulls = 0
    cows = 0

    for i in range(4):
        if tajne_cislo[i] == hadani[i]:
            bulls += 1
        elif hadani[i] in tajne_cislo:
            cows += 1

    return bulls, cows

def main():
    print("Hi There")
    print(cara)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game..")
    print(cara)

    tajne_cislo = generuj_tajne_cislo()
    pokusy = 0
    start_cas = time.time()

    print(f"(Debug) Tajné číslo je: {tajne_cislo}")  

    
    while True:
        hadani = input("Enter a number:")
        print(cara)
        
        if len(hadani) != 4 or not hadani.isdigit() or hadani[0] == '0' or len(set(hadani)) != 4:
            print("Invalid input. Please enter 4 unique digits that don't start with 0.")
            continue

        pokusy += 1
        bulls, cows = vyhodnot_hadani(tajne_cislo, hadani)
        print(f"{bulls} bull(s), {cows} cow(s)")
        print(cara)

        if bulls == 4:
            uplynuly_cas = time.time() - start_cas  # Výpočet uplynulého času
            print(f"Correct, you've guessed the right number in {pokusy} guesses!")  # 
            print(f"It took you {uplynuly_cas:.3f} seconds.")  # Zobrazení času
            print(cara)
            print(f"That's {ziskej_hodnoceni(pokusy)}")
            print(cara)
            break

#HODNOCENÍ
def ziskej_hodnoceni(pocet_pokusu):
    """Vrátí hodnocení hráče na základě počtu pokusů."""
    if pocet_pokusu <= 4:
        return "amazing"
    elif pocet_pokusu <= 7:
        return "average"
    else:
        return "not so good"

if __name__ == "__main__":
    main()