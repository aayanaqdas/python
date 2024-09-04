from random import randint


# 01. Kast en terning en gang, se utfall.
'''
kast = randint(1,6)
print("\nTerningkastets resultat:", kast)
'''



# 02. Kast en terning, for-loop med 10 kast, se utfall.
'''
antall = 10 
for i in range(antall):
    kast = randint(1,6)
    print("Terningkast", i, "ga:", kast)

'''

# 03. Kast en terning, input av antall kast, for-loop, se utfall.
'''
antall = int(input("\nskriv antall kast: "))
print("\n")
for i in range(antall):
    kast = randint(1,6)
    print("Terningkast", i, "ga:", kast)
'''

# 04. Kast en terning, input av antall kast, legg i liste,for-loop, se utfall.
'''
antall = int(input("skriv antall kast: "))
kastliste = []
for i in range(antall):
    kast = randint(1,6)
    kastliste.append(kast)
for b in range(len(kastliste)):
    print("kast nr. ", b, "ga ", kastliste[b])

'''

# 05. Kast en terning, input av antall kast, legg i liste, nested for-loop, se utfall.
'''
antall = int(input("Skriv antall kast:  "))
kastliste = []
muligheter = [1,2,3,4,5,6]

treff = [0,0,0,0,0,0]
for a in range(antall):
    kast = randint(1,6)
    kastliste.append(kast)
    print("kast nr. ",(a+1),"ga ", kast)

for b in range(len(kastliste)):
    for c in range(len(muligheter)):
        if kastliste[b] == muligheter[c]:
            treff[c] = treff[c]+1

for d in range(len(treff)):
    print("Terningtall", (d+1), "ble trukket ", treff[d], "ganger.")

'''

# 06. Kast en terning, input av antall kast, legg i liste, nested for-loop, barchart.
