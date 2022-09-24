import random
szam = random.randint(1,2)
fej_iras = input('Fej vagy írás?')
fej = ('fej')
iras = ('írás')
iras = 1
fej = 2
if szam == fej:
    print('Eltaláltad')
elif szam != fej:
    print('Nem találtad el')
elif szam == iras:
    print('Eltaláltad')
elif szam != iras:
    print('Nem találtad el')
