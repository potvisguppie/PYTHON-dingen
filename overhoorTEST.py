import os

DELETE = 'd'
EXTENSIE = '.txt'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 40
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = ':'
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'


def leeg_scherm():
    os.system('cls' if os.name == 'nt' else 'clear')


def lees_woordenlijst(bestandsnaam):
    woordenlijst = {}
    try:
        with open(bestandsnaam + EXTENSIE, 'r') as f:
            for line in f:
                if len(line.strip().split(SCHEIDER)) == 2:
                    woord1, woord2 = line.strip().split(SCHEIDER)
                    woordenlijst[woord1] = woord2
    except FileNotFoundError:
        print(f"Bestand {bestandsnaam + EXTENSIE} niet gevonden.")
    return woordenlijst


def nieuwe_lijst_maken():
    print_header()
    print_regel("Hoe wil je je nieuwe lijst noemen?")
    print_footer()
    nieuwe_naam = input('').strip()
    with open(nieuwe_naam + EXTENSIE, "a"):
        pass
    return nieuwe_naam


def schrijf_woorden_lijst(bestandsnaam, woordenlijst):
    with open(bestandsnaam + EXTENSIE, 'w') as f:
        for woord1, woord2 in woordenlijst.items():
            f.write(f"{woord1}{SCHEIDER}{woord2}\n")


def voeg_woorden_toe(bestandsnaam):
    woordenlijst = lees_woordenlijst(bestandsnaam)
    woord1 = ''
    while woord1 != STOPPEN:
        leeg_scherm()
        print_header()
        print_regel("Welk woord wil je toevoegen? Klik q om te stoppen")
        print_footer()
        woord1 = input().lower()
       
        if woord1 != STOPPEN:
            leeg_scherm()
            print_header()
            print_regel("En wat is de vertaling daarvan? ")
            print_footer()
            woord2 = input().lower()
            woordenlijst[woord1] = woord2
            schrijf_woorden_lijst(bestandsnaam, woordenlijst)
    return woordenlijst


def overhoren(woordenlijst):
    woordenlijst2 = woordenlijst.copy()  
    for woord1, woord2 in woordenlijst2.items():  
        leeg_scherm()
        print_header()
        print_regel(f"Wat is de betekenis van '{woord1}'?")
        print_regel(f"Type '{STOPPEN}' om te stoppen of '{DELETE}' om het woord te verwijderen")
        print_footer()
        antwoord = input("")
        if antwoord == woord2:
            leeg_scherm()
            print_header()
            print_regel("Goed gedaan!")
            print_footer()
        elif antwoord == STOPPEN:
            break
        elif antwoord == DELETE:
            verwijder_woord(woord1, woordenlijst)
        else:
            leeg_scherm()
            print_header()
            print_regel(f"Helaas, dat is fout. Dit was het antwoord: {woord2} |klik k om door te gaan")
            print_footer()
            doorgaan = input("")
            if doorgaan == "k":
                print("")
            
    return woordenlijst    



def print_afscheid():
    try:
        with open("afscheid.txt", 'r') as f:
            afscheid = f.read()
            print(afscheid)
    except FileNotFoundError:
        print("Afscheid bestand niet gevonden.")


def print_footer():
    print("|" + " " * (SCHERMBREEDTE - 2) + "|")
    print("=" * SCHERMBREEDTE)


def print_header():
    print("=" * SCHERMBREEDTE)
    print("|" + " " * (SCHERMBREEDTE - 2) + "|")


def print_menu(lijst_naam):
    print_header()
    print_regel(f"Woordenlijst: {lijst_naam}")
    print_regel(f"{OVERHOREN} - overhoor de geselecteerde woordenlijst")
    print_regel(f"{TOEVOEGEN} - voeg woorden toe aan de geselecteerde woordenlijst")
    print_regel(f"{KIES_LIJST} - Selecteer een andere woordenlijst")
    print_regel(f"{NIEUWE_LIJST} - Maak een nieuwe woordenlijst")
    print_regel(f"{STOPPEN} - Stoppen")
    print_footer()


def print_regel(inhoud=''):
    print(f"| {inhoud:<{SCHERMBREEDTE - 4}} |")


def verwijder_woord(woord, woordenlijst):
    if woord in woordenlijst:
        del woordenlijst[woord]
        print(f"'{woord}' is verwijderd uit de lijst.")
        
    else:
        print(f"'{woord}' niet gevonden in de lijst.")
    return woordenlijst


def kies_woordenlijst():
    leeg_scherm()
    print_header()
    print_regel("Welke woordenlijst wil je selecteren?")
    print_footer()
    lijst_naam = input('').strip()
    return lijst_naam


def main():
    lijst_naam = STANDAARD_LIJST
    woordenlijst = lees_woordenlijst(lijst_naam)
    vraag = ""
    while vraag != STOPPEN:
        leeg_scherm()
        print_menu(lijst_naam)
        vraag = input("Wat wil je doen? ").strip().lower()
        if vraag == OVERHOREN:
            woordenlijst = overhoren(woordenlijst)
        elif vraag == TOEVOEGEN:
            woordenlijst = voeg_woorden_toe(lijst_naam)
        elif vraag == NIEUWE_LIJST:
            lijst_naam = nieuwe_lijst_maken()
            woordenlijst = {}
        elif vraag == KIES_LIJST:
            lijst_naam = kies_woordenlijst()
            woordenlijst = lees_woordenlijst(lijst_naam)
        elif vraag == STOPPEN:
            print_afscheid()
        else:
            print("Ongeldige keuze, probeer opnieuw.")

main()
