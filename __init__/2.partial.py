from functools import partial
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
    part_class = {
        1:partial(AceCard,'A'),
        11:partial(FaceCard,'J'),
        12:partial(FaceCard,'Q'),
        13:partial(FaceCard,'K')
    }.get(rank,partial(NumberCard,str(rank)))
    return part_class(suit)

b=[card(rank,suit) for rank in range(1,14) for suit in ("C","D","H","S")]
for i in b:
    print(i.display())