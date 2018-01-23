'''
namedtuple()函数根据提供的参数创建一个新类
'''

from collections import namedtuple

BlackJackCard = namedtuple('BlackJackCard','rank,suit,hard,soft')

def card(rank,suit):
    if rank == 1:
        return BlackJackCard('A',suit,1,11)
    elif 2 <= rank < 11 :
        return BlackJackCard(str(rank),suit,rank,rank)
    elif rank == 11 :
        return BlackJackCard('J',suit,10,10)
    elif rank == 12 :
        return BlackJackCard('Q',suit,10,10)
    elif rank == 13 :
        return BlackJackCard('K',suit,10,10)

a=card(1,'s')
print(a.__class__.mro())

class AceCard(BlackJackCard):
    __slots__ = ()
    def __new__(cls, rank, suit):
        return super().__new__(AceCard,'A',suit,1,11)
    def display(self):
        return (self.rank+'-'+self.suit+'-'+str(self.hard))

a=AceCard(1,'B')
print(a.display())