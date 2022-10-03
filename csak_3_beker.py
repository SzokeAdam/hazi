nevek = []
adat = None
while len(nevek) != 3:
    adat = input('Adj meg egy keresztnevet: ')
    if adat != '':
        nevek.append(adat)
    if len(nevek) == 3:
        print((' ').join (nevek))
print('Program vége')