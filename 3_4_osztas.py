szam = int(input('Adj meg egy számot:'))
if szam % 3 == 0 and szam % 4 == 0:
    print('3-mal és 4-gyel is osztható')
if szam % 3 != 0 and szam % 4 != 0:
    print('Sem 3-mal, sem 4-gyel nem osztható')
elif szam % 3 == 0:
    print('Csak 3-mal osztható')
elif szam % 4 == 0:
    print('Csak 4-gyel osztható')
