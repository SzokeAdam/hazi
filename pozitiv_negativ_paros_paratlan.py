szam = int(input('Adj meg egy egész számot'))
if szam > 0 and szam % 2 == 0:
    print('A számod pozítiv és páros')
elif szam < 0 and szam % 2 != 0:
    print('A számod negatív és páratlan')
