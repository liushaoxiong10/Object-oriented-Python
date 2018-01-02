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

class CardFactory:
    def rank(self,rank):
        self.class_,self.rank_str={
            1:(AceCard,'A'),
            11:(FaceCard,'J'),
            12:(FaceCard,'Q'),
            13:(FaceCard,'K')
        }.get(rank,(NumberCard,str(rank)))
        return self
    def suit(self,suit):
        return self.class_(self.rank_str,suit)

card=CardFactory()

deck=[card.rank(r+1).suit(s) for r in range(13) for s in ('C','D','H','S')]
for i in deck:
    print(i.display())