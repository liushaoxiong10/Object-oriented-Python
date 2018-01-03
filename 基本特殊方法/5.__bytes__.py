'''
Bytes 对象是由单个字节作为基本元素（8位，取值范围 0-255）组成的序列，为不可变对象。
'''

class Ace:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def dis(self):
        return ("Ace {0} {1}".format(self.rank,self.suit))
class Num:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def dis(self):
        return ("Num {0} {1}".format(self.rank,self.suit))

def card_from_bytes(buffer):
    string=buffer.decode("utf8")
    assert string[0] == "("and string[-1] ==")"
    code,rank_number,suit = string[1:-1].split()
    class_ = {'A':Ace,'N':Num}[code]
    return class_(int(rank_number),suit)
card="(A 2 Two)"
card=bytes(card,encoding="utf8")
print(card)
print(card_from_bytes(card).dis())