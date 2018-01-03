'''
__lt__  <
__le__  <=
__gt__  >
__ge__

'''

class Black:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def __lt__(self, other):
        print("Compare {0} < {1}".format(self,other))
        return self.rank < other.rank
    def __str__(self):
        return "{rank} {suit}".format(**self.__dict__)

a=Black(1,"A")
print(a)
b=Black(2,"B")
print(a<b)