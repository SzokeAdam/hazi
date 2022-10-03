szavak = []
adat = None
while adat != '':
    adat = input('Adj meg egy keresztnevet: ')
    if adat[0:1] != 'a':
        adat = input('Adj meg egy keresztnevet: ')
    if adat[0:1] == 'a':
        szavak.append(adat)
print((',').join (szavak))