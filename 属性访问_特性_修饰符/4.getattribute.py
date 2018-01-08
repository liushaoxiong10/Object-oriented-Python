'''
__getattribute__() :提供对底层的一些操作，默认的实现逻辑是先从内部的__dict__(或__slots__)中查找已知属性。如果属性没有找到则调用
                    __getattr__()函数
重写的目的：1.有效阻止属性访问
          2.可以仿照__getattr__()函数的工作方式来创建新属性，在这种情况下可以绕过__getattribute__()的实现逻辑
          3.使得属性执行单独或不同任务，但这样会降低程序的可读性和可维护性
          4.可以改变修饰符的行为
当实现__getattribute__()方法时，将阻止任何内部属性访问函数体
'''

class Card:
    def __init__(self,rank,suit,hard,soft):
        super().__setattr__('rank',rank)
        super().__setattr__('suit',suit)
        super().__setattr__('hard',hard)
        super().__setattr__('soft',soft)
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError("Cannot set {name }".format(name = key ))
        raise AttributeError("'__class__.__name__' has no attribute '{name}'".format(__class__ = self.__class__ ,name = key ))
    def __getattribute__(self, name):
        if name.startswith('_'): raise AttributeError
        return object.__getattribute__(self,name)

c=Card('A','C',1,11)
print(c.rank)
try:
    c.rank='J'
    print(c.rank)
except AttributeError:
    print('Error')
try:
    print(c.__dict__)
except AttributeError:
    print('Error')

