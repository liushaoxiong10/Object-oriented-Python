import random

class Card:
    def __init__(self,rank,suit,hard,soft):
        self.suit=suit
        self.rank=rank
        self.hard,self.soft=hard,soft
    def display(self):
        return (self.rank,self.suit,self.hard,self.soft)

class NumberCard(Card):
    def __init__(self,rank,suit):
        super().__init__(str(rank),suit,rank,rank)


class AceCard(Card):
    def __init__(self,rank,suit):
        super().__init__("A",suit,1,11)


class FaceCard(Card):
    def __init__(self,rank,suit):
        super().__init__({
            11:'J',
            12:'Q',
            13:'K'
        }[rank],suit,10,10)

class CardFactory:
    def rank(self,rank,suit):
        self.class_,self.rank_str={
            1:(AceCard,'A'),
            11:(FaceCard,'J'),
            12:(FaceCard,'Q'),
            13:(FaceCard,'K')
        }.get(rank,(NumberCard,str(rank)))
        return self.class_(rank,suit)

card=CardFactory()

deck=[card.rank(r+1,s) for r in range(13) for s in ('C','D','H','S')]
random.shuffle(deck)
print(len(deck))
for i in deck:
    print (i.display())

