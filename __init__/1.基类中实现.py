class Card:
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
        self.hard,self.soft=self._points()
    def display(self):
        return (self._points(),self.suit)

class NumberCard(Card):
    def _points(self):
        return int(self.rank),int(self.rank)

class AceCard(Card):
    def _points(self):
        return 1,11

class FaceCard(Card):
    def _points(self):
        return 10,10

def card(rank,suit):
    if rank == 1:return AceCard('A',suit)
    elif 2<= rank <11 :return NumberCard(str(rank),suit)
    elif 11<= rank<14:
        name ={11:'J',12:'Q',13:'K'}[rank]
        return FaceCard(name,suit)
    else:
        raise Exception("Rank out of range")
b=[card(rank,suit) for rank in range(1,14) for suit in ("C","D","H","S")]
for i in b:
    print(i.display())