import random
szam = random.randint (1, 5)
adat = int(input('Adj meg egy számot 1 és 5 között'))
print (szam)
if szam == adat:
    print ('A gép úgyan arra gondolt mint te.')
elif adat < szam:
    print ('A gép száma nagyobb mint a tiéd')
elif adat > szam:
    print ('A gép száma kisseb mint a tiéd')