# ez a program bekéri a sugarat és kiszámolja a kör kerületét és területét
adat = input('Add meg a kör sugarát')
szam = (int(adat))
import math 
PI = math.pi
kerulet = (2*PI)*szam
terulet = PI*(szam*szam)
print (kerulet)
print (terulet)