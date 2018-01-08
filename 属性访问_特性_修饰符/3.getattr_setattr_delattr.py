'''
__setattr__() :用于属性的创建和赋值
__getattr__() :1.如果属性已经被赋值，直接返回属性值
               2.如果属性没有被赋值，将使用__getattr__()的返回值
               3.如果找不到相关属性，要记得跑出AttributeError异常
__delattr__() :用于删除属性
__dir__() :返回属性名称列表

'''

class Card:
    __slots__ = ('rank','suit')
    def __init__(self,rank,suit):
        super().__setattr__('rank',rank)
        super().__setattr__('suit',suit)
    def __str__(self):
        return "{0.rank} {0.suit} ".format(self)
    def __setattr__(self, name, value):
        raise AttributeError("'{__class__.__name__}' has no attribute '{name}'".format(___class__=self.__class__ , name=name))

card=Card(3,'C')
print(card.rank)

print(card)
