DELETE = 'd'
EXTENSIE = '.wrd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = ':'
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'

    kies_lijst(lijst_naam)


    leeg_scherm()
        Maakt het terminalscherm leeg

        Gebruikt: -
        Parameters: -
        # Returnwaarde: 


def lees_woordenlijst():
	f = open('C:\\Users\Admin\Downloads\message (2).txt')
	woordenlijst = {}
	for line in f:
		if len(line.strip('\n').split(SCHEIDER)) == 2:
			woord1, woord2 = line.strip('\n').split(SCHEIDER)
			woordenlijst[woord1] = woord2
	f.close()
	return woordenlijst

print(lees_woordenlijst())

    main()
        Laat een keuzemenu zien

        Op zijn minst zijn de volgende keuzes mogelijk:
         - nieuwe woordenlijst maken
         - veranderen van woordenlijst
         - woorden toevoegen aan een woordenlijst
         - woordenlijsten overhoren
         - stoppen met het programma

        De gebruiker kan vervolgens steeds nieuwe keuzes blijven maken.

        Gebruikt: STANDAARD_LIJST, KIES_LIJST, OVERHOREN, TOEVOEGEN, EXTENSIE, STOPPEN
        Parameters: Geen
        Returnwaarde: Geen

    nieuwe_lijst_naam()
        Gebruikt: -
        Parameters: -
        Returnwaarde: de lijst_naam van de nieuw gekozen lijst

    overhoren(woordenlijst)
        Blijf woorden overhoren totdat de gebruiker aangeeft te willen stoppen.

        Gebruikt: STOPPEN
        Parameters: de woordenlijst die overhoord moet worden
        Returnwaarde: -

    print_afscheid()
        Print een afscheidboodschap nadat het programma is afgesloten

        Gebruikt: SCHERMHOOGTE, SCHERMBREEDTE
        Parameters: -
        Returnwaarde: -

    print_footer()
        Print het volgende over de hele breedte van het scherm:
        |             |
        ===============
        Dus een volle regel met '='-tekens en een regel die begint en eindigt met een '|'.

        Gebruikt: SCHERMBREEDTE
        Parameters: -
        Returnwaarde: -

    print_header()
        Print het volgende over de hele breedte van het scherm:
        ===============
        |             |
        Dus een volle regel met '='-tekens en een regel die begint en eindigt met een '|'.

        Gebruikt: SCHERMBREEDTE
        Parameters: -
        Returnwaarde: -

    print_menu(lijst_naam)
        Print het (keuze)menu inclusief de geselecteerde lijst

        Gebruikt: SCHERMHOOGTE, SCHERMBREEDTE
        Parameters: De naam van de geselecteerde woordenlijst
        Returnwaarde: -

    print_regel(inhoud='')
        print_regel() print de inhoud links uitgelijnd uit.
        Voor de inhoud wordt '| ' gezet en rechts uitgelijnd ' |'.
        Bijvoorbeeld:
        SCHERMBREEDTE = 30
        inhoud = "Mooi zeg"
        Uitvoer:
        | Mooi zeg                   |

        Gebruikt: SCHERMBREEDTE
        Parameters: de string die geprint moet worden in de regel
        Returnwaarde: -

    schrijf_woordenlijst(bestandsnaam, woordenlijst)
        Schrijft de woordparen weg naar het bestand genaamd 'bestandsnaam'.
        De oude inhoud van het bestand wordt overschreven!

        Gebruikt: SCHEIDER
        Parameter: naam van het bestand waar de woordenlijst in geschreven wordt, woordenlijst die weggeschreven wordt
        Returnwaarde: -

    verwijder_woord(woord, woordenlijst)
        Vraagt of gebruiker zeker weet of er verwijderd moet worden.
        Verwijdert het woord en de vertaling uit de lijst als dit zo is.

        Gebruikt: -
        Parameters: het woord dat verwijderd moet worden, de woordenlijst waaruit verwijderd moet worden
        Returnwaarde: -

    voeg_woorden_toe(woordenlijst, lijst_naam)
        Vraag de gebruiker steeds om woordenparen en voeg ze toe aan de lijst.
        Stop als de gebruiker aangeeft te willen stoppen.

        Gebruikt: SCHEIDER, STOPPEN
        Parameters: de woordenlijst waarin toegevoegd moet worden, de lijst_naam van deze woordenlijst
        Returnwaarde: -

