adat = input('Jön-e Henrik kosarazni?')
adat2 = input('Jön-e Hanna kosarazni?')
igen = ('igen')
nem = ('nem')
if adat == igen and adat2 == igen:
    print('Mind a ketten jönnek kosarazni')
elif adat == nem and adat2 == igen:
    print('Csak az egyikük jön kosarazni')
elif adat == igen and adat2 == nem:
    print('Csak az egyikük jön kosarazni')
elif adat == nem and adat2 == nem:
    print('Egyikük sem jön kosarazni')
