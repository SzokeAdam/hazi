szamok = []
import random
gene = 1
while gene != 11:
    szam = random.randint(0,50)
    if szam % 4 == 0:
        szamok.append(szam)  
    gene = gene + 1
print(szamok)