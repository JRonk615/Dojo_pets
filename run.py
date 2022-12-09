from Pets import Ninja, Pet, Doberman

murphy = Doberman('murphy', 'doberman', ['shake', 'sit', 'play dead'], 100, 10)
dogo = Pet('dogo', 'Pitbull', ['shake', 'sit', 'play dead'], 100, 10)
Jordan = Ninja('Jordan', 'Ronk', ['biscuits', 'bone', 'bacon'], 'Lone Wolf dog food', dogo)



print(murphy.tricks)
Jordan.walk(5)
Jordan.feed()