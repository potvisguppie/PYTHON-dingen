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

def main():
	leeg_scherm()
	print_header()
	print_regel(OVERHOREN + " - overhoor de geselecteerde woordenlijst")
	print_regel(TOEVOEGEN + " - voeg woorden toe aan de geselecteerde woordenlijst")
	print_regel(KIES_LIJST + " - Selecteer een andere woordenlijst")
	print_regel(NIEUWE_LIJST + " - Maak een nieuwe woordenlijst")
	print_regel(STOPPEN + " - Stoppen  ")
	print_footer()

	vraag = input(" Wat wil je doen?")
	if vraag == OVERHOREN:
		woordenlijst = lees_woordenlijst()
		overhoren(woordenlijst)
	
	elif vraag == TOEVOEGEN:
		nieuwe_naam = nieuwe_lijst_maken()
		voeg_woorden_toe( nieuwe_naam + EXTENSIE)

	elif vraag == NIEUWE_LIJST:
		leeg_scherm()
		nieuwe_naam = nieuwe_lijst_maken()
		voeg_woorden_toe(nieuwe_naam) 
	
	elif vraag == KIES_LIJST:
		woordenlijst_naam = kies_woordenlijst()

	
	elif vraag == STOPPEN:
		leeg_scherm()
		quit()

def lees_woordenlijst():
	f = open('E:\\PYTHON dingen\message (2)' + EXTENSIE)
	woordenlijst = {}
	for line in f:
		if len(line.strip('\n').split(SCHEIDER)) == 2:
			woord1, woord2 = line.strip('\n').split(SCHEIDER)
			woordenlijst[woord1] = woord2
	f.close()
	return woordenlijst


def nieuwe_lijst_maken():
	print_header()
	print_regel("Hoe wil je je nieuwe lijst noemen?")
	print_footer()
	nieuwe_naam = input('')
	f = open(nieuwe_naam + EXTENSIE, "a")
	return nieuwe_naam


def schrijf_woorden_lijst(bestandsnaam, woordenlijst):
	print()	


def voeg_woorden_toe(nieuwe_naam):
	'''leg uit functie'''
	f = open(nieuwe_naam , 'w')
	doorgaan = True
	while doorgaan:
		leeg_scherm()
		print_header()
		print_regel("Welk woord wil je toevoegen? Klik q om te stoppen")
		print_footer()
		woord1 = input().lower()
		if woord1 == STOPPEN:
			doorgaan = False
			f.close()
			main()
		else:
			#vraagt vertaling
			leeg_scherm()
			print_header()
			print_regel("En wat is de vertaling daarvan? ")
			print_footer()
			woord2 = input().lower()
			f.write(woord1 + ":" + woord2 + "\n")
	f.close()


def overhoren(woordenlijst):
	for woord1, woord2 in woordenlijst.items():
		leeg_scherm()
		print_header()
		print_regel("Wat is de betekenis van '{}' ".format(woord1))
		print_regel("Type '{}' om te stoppen of '{}' om het woord te verwijderen".format(STOPPEN, DELETE))
		print_footer()
		antwoord = input("")
		if antwoord == woord2:
			print_header()
			print_regel("goed gedaan! ")
			print_footer()
		if antwoord == STOPPEN:
			main()
			break
		if antwoord == DELETE:
			verwijder_woord()
		else:
			print_header()
			print_regel("helaas dat is niet goed. Dit was het antwoord " + woord2)
			print_footer()

def verwijder_woord(woord, woordenlijst, woordenlijst_naam):
	woordenlijst = woordenlijst_naam + EXTENSIE
	del woordenlijst[woord]
	schrijf_woorden_lijst(woordenlijst_naam, woordenlijst)
	

def print_regel(regel=""):
  	print(("| {:" + str(SCHERMBREEDTE -4)+ "} |").format(regel))

def print_header():
	print("="*SCHERMBREEDTE)
	print("|" +  " "*(SCHERMBREEDTE -2)  +  "|")


def print_footer():
	print("|" +  " "*(SCHERMBREEDTE -2)  +  "|")
	print("="*SCHERMBREEDTE)

def kies_woordenlijst():
	leeg_scherm()
	print_header()
	print_regel("Welke woordenlijst wil je selecteren")
	print_footer()
	woordenlijst_naam = input('')

	return woordenlijst_naam


def leeg_scherm():
  os.system('cls||clear')


main()


