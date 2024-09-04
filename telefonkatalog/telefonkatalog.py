# -*- coding: utf-8 -*-


import sqlite3  # Importerer biblioteket SQLite3, som brukes til å jobbe med en SQL-database i Python

conn = sqlite3.connect('telefonkatalog.db') # Vi kobler til en SQLite database med funksjonen connect(). Hvis filen 'telefonkatalog.db' ikke finnes, lages den automatisk

cursor = conn.cursor()  # Lager et objekt som lar oss bruke SQL på databasen

# Opprett en tabell hvis den ikke allerede eksisterer. Den heter 'personer' og har kolonnene 'fornavn', 'etternavn' og 'telefonnummer'. Hvis tabellen finnes fra før skjer ingenting.
cursor.execute('''CREATE TABLE IF NOT EXISTS personer (
                fornavn TEXT,
                etternavn TEXT,
                telefonnummer TEXT
            )''')

conn.commit()  # Lagrer endringene til databasen. Denne må kalles etter alle endringer i databasen.

# telefonkatalog = [] #Liste format ["fornavn", "etternavn", "telefonnummer"]


def visAllePersoner():
    cursor.execute("SELECT * FROM personer")
    resultater = cursor.fetchall()
    if not resultater:
        print("***********************************************************************************")
        print("Det er ingen registrerte personer i katalogen: ")
        print("***********************************************************************************")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()
    else: 
        print("***********************************************************************************")
        for personer in resultater: 
            print("* Fornavn: {:15s} Etternavn: {:15s} Telefonnummer: {:8s}     *".format(personer[0], personer[1], personer[2]) )
        print("***********************************************************************************")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()


# Funksjon som legger til en ny person i databasen
def legg_til_person_i_db(fornavn, etternavn, telefonnummer):
    cursor.execute("INSERT INTO personer (fornavn, etternavn, telefonnummer) VALUES (?, ?, ?)", 
                   (fornavn, etternavn, telefonnummer))
    conn.commit()

# Funksjon som sletter en person fra databasen basert på fornavn, etternavn og telefonnummer
def slett_person_fra_db(fornavn, etternavn, telefonnummer):
    cursor.execute("DELETE FROM personer WHERE fornavn=? AND etternavn=? AND telefonnummer=?",
              (fornavn, etternavn, telefonnummer))
    conn.commit()

def printMeny():
    print("--------------- Telefonkatalog ---------------")
    print("| 1. Legg til ny person                      |")
    print("| 2. Søk opp person eller telefonnummer      |")
    print("| 3. Vis alle personer                       |")
    print("| 4. Fjern person                            |")
    print("| 5. Endre oppføring                         |")
    print("| 6. Avslutt                                 |")
    print("----------------------------------------------")

    menyvalg = input("Skriv inn tall for å velge fra menyen: ")
    utfoerMenyvalg(menyvalg)

def utfoerMenyvalg(valgtTall):
    if valgtTall == "1": #input returnerer string, derfor "1"
        print(valgtTall)
        registrerPerson()
    elif valgtTall == "2":
        sokPerson()
        printMeny()
    elif valgtTall == "3":
        visAllePersoner()
    elif valgtTall == "4":
        fjernPerson()
        printMeny()
    elif valgtTall == "5":
        #endreOppføring()
        printMeny()
    elif valgtTall == "6":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if (bekreftelse == "J" or bekreftelse == "j"): #Sjekker bare for ja
            conn.close()
            exit()
    else: 
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-6: ")
        utfoerMenyvalg(nyttForsoek)

def registrerPerson():
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    telefonnummer = input("Skriv inn telefonnummer: ")

    legg_til_person_i_db(fornavn, etternavn, telefonnummer) # Legger til informasjonen fra input-feltene i databasen som en ny rad

    # nyRegistrering = [fornavn, etternavn, telefonnummer]
    # telefonkatalog.append(nyRegistrering)

    print("{0} {1} er registrert med telefonnummer {2}".format(fornavn, etternavn, telefonnummer))
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()

def fjernPerson():
    cursor.execute("SELECT * FROM personer")
    resultater = cursor.fetchall()
    if not resultater:
        print("Det er ingen registrerte personer i katalogen: ")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()

    else:
        print("Fjern registrering: ")
        fornavn = input("Skriv inn fornavn: ")
        etternavn = input("Skriv inn etternavn: ")
        telefonnummer = input("Skriv inn telefonnummer: ")

    found = False
    for person in resultater:
        if person[0] == fornavn and person[1] == etternavn and person[2] == telefonnummer:
            found = True
            break

    if found:
        # fjernRegistrering = [fornavn, etternavn, telefonnummer]
        # telefonkatalog.remove(fjernRegistrering)
        slett_person_fra_db(fornavn, etternavn, telefonnummer)
        print("{0} {1} er fjernet fra katalogen".format(fornavn, etternavn))
    else:
        print("{0} {1} {2} finnes ikke i katalogen".format(fornavn, etternavn, telefonnummer))
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()



# def endreOppføring():
#     if not telefonkatalog:
#         print("Det er ingen registrerte personer i katalogen: ")
#         input("Trykk en tast for å gå tilbake til menyen")
#         printMeny()
#     else:
#         print("Endre oppføring: ")
#         fornavn = input("Skriv inn fornavn: ")
#         etternavn = input("Skriv inn etternavn: ")
#         telefonnummer = input("Skriv inn telefonnummer: ")

#         found = False
#         for person in telefonkatalog:
#             if person[0] == fornavn and person[1] == etternavn and person[2] == telefonnummer:
#                 found = True
#                 break

#         #fjernRegistrering = [fornavn, etternavn, telefonnummer]
#         #telefonkatalog.remove(fjernRegistrering)


#         if found:
#             print("Ny oppføring: ")
#             nyttFornavn = input("Nytt fornavn: ")
#             nyttEtternavn = input("Nytt etternavn: ")
#             nyttTelefonnummer = input("Nytt telefonnummer: ")
#             telefonkatalog[telefonkatalog.index(person)] = [nyttFornavn, nyttEtternavn, nyttTelefonnummer]
#             #nyRegistrering = [nyttFornavn, nyttEtternavn, nyttTelefonnummer]
#             #telefonkatalog.append(nyRegistrering)

#             print("{0} {1} {2} er endret til: ".format(fornavn, etternavn, telefonnummer), "{0} {1} {2}".format(nyttFornavn, nyttEtternavn, nyttTelefonnummer))
#         else:
#             print("{0} {1} {2} finnes ikke i katalogen".format(fornavn, etternavn, telefonnummer))
#             input("Trykk en tast for å gå tilbake til menyen")
#             printMeny()
 




def sokPerson():
    cursor.execute("SELECT * FROM personer")
    resultater = cursor.fetchall()
    if not resultater:
        print("Det er ingen registrerte personer i katalogen")
        printMeny()
    else: 
        print("1. Søk på fornavn")
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. Tilbake til hovedmeny")

        sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
        if sokefelt == "1":
            navn = input("Fornavn: ")
            finnPerson("fornavn", navn)
        elif sokefelt == "2":
            navn = input("Etternavn: ")
            finnPerson("etternavn", navn)
        elif sokefelt == "3":
            tlfnummer = input("Telefonnummer: ")
            finnPerson("telefonnummer", tlfnummer)
        elif sokefelt == "4":
            printMeny()
        else: 
            print("Ugyldig valg. Velg et tall mellom 1-4: ")
            sokPerson()

# typesøk angir om man søker på fornavn, etternavn, eller telefonnummer
def finnPerson(typeSok, sokeTekst):
    if typeSok == "fornavn":
        cursor.execute("SELECT * FROM personer WHERE fornavn=?", (sokeTekst,))
    elif typeSok == "etternavn":
        cursor.execute("SELECT * FROM personer WHERE etternavn=?", (sokeTekst,))
    elif typeSok == "telefonnummer":
        cursor.execute("SELECT * FROM personer WHERE telefonnummer=?", (sokeTekst,))

    resultater = cursor.fetchall()
    if not resultater:
        if typeSok == "fornavn":
            print("Finner ingen personer med fornavn " + sokeTekst)
        elif typeSok == "etternavn":
            print("Finner ingen personer med etternavn " + sokeTekst)
        elif typeSok == "telefonnummer":
            print("Telefonnummer " + sokeTekst + " er ikke registrert.")
    else:
        for personer in resultater:
            if typeSok == "telefonnummer":
                print("Telefonnummer {0} tilhører {1} {2}".format(personer[2], personer[0], personer[1]))
            else:
                print("{0} {1} har telefonnummer {2}".format(personer[0], personer[1], personer[2]))

printMeny() #Starter programmet ved å skrive menyen første gang