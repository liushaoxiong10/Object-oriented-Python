'''
这个抽象基类使用abstractmethod装饰器定义了3个抽象方法，任何试图实现这个抽象类的子类都必须实现这3个方法
__subclasshook__方法需要这3个方法都被实现
__dict__ 特性用于存储类中定义的方法名和特性名，存储了类的主体
__mro__  特性中记录了解析方法的顺序，记录了当前类层次结构的顺序
'''
from abc import ABCMeta, abstractclassmethod
class AbstractBettingStrategy(metaclass=ABCMeta):
    __slots__ = ()
    @abstractclassmethod
    def bet(self,hand):
        return 1
    @abstractclassmethod
    def record_win(self,hand):
        pass
    @abstractclassmethod
    def record_loss(self,hand):
        pass
    @classmethod
    def __subclasshook__(cls,subclass):
        if cls is Hand:
            if (any("bet" in B.__dict__ for B in subclass.__mro__)
                and any("record_win" in B.__dict__ for B in subclass.__mro__)
                and any("record_loss" in B.__dict__ for B in subclass.__mro__)
            ):
                return True
        return NotImplemented

