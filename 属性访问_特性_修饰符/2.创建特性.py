'''
主动计算：每当更新特性值时，其他相关特性值都会立即被重新计算
延迟计算：晋档访问特性时，才会触发计算过程
@property 将一个方法设置为属性
'''
class student:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if not isinstance(value,int):
            raise "Type Error"
        self._age=value
s=student
s.age=11
print(s.age)
'''
延迟计算
'''
class Hand:
    def __init__(self,*cards):
        self._cards=list(cards)
    @property
    def card(self):
        return self._cards
    @card.setter
    def card(self,aCard):
        self._cards.append(aCard)
    @card.deleter
    def card(self):
        self._cards.pop(-1)
    @property
    def total(self):
        sum=0
        for i in self._cards:sum+=i
        return sum
h=Hand(1,2,3,4,5,6,7)
print(h.card)
print(h.total)
h.card=8
print(h.card)
print(h.total)
del h.card
print(h.card)
print(h.total)

'''
主动计算
'''
class Hand:
    def __init__(self,*cards):
        self._cards=list(cards)
    @property
    def card(self):
        return self._cards
    @card.setter
    def card(self,aCard):
        self._cards.append(aCard)
        self.total()
    @card.deleter
    def card(self):
        self._cards.pop(-1)
        self.total()
    def total(self):
        sum=0
        for i in self._cards:sum+=i
        print(sum)

h=Hand(1,2,3,4,5,6,7)
h.card=8
h.card=9
del h.card