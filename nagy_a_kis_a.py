szavak = []
adat = input('Adj meg egy keresztnevet: ')
while adat != '':
    if adat[0:1] == 'A':
        szavak.append(adat)
        
    elif adat[0:1] == 'a':
        szavak.append(adat)
        
    if adat[0:1] != 'A':
        adat = input('Adj meg egy keresztnevet: ')
        
    elif adat[0:1] != 'a':
        adat = input('Adj meg egy keresztnevet: ')
        
print((',').join (szavak))