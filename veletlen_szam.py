import random
veletlen_szam = random.randint(1,3)
adat = int(input('Adj meg egy számot 1 és 3 között:'))
print('A gép száma:')
print (veletlen_szam)
if adat == veletlen_szam:
    print('A megadott szám megeggyezik a gép általi számmal')
if adat > veletlen_szam:
    print('A számod nagyobb mint a gép általi szám')
if adat < veletlen_szam:
    print('A gép száma nagyobb mint a te számod')