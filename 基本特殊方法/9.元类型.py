'''
元类就是那个帮你创建类的"家伙"。
为了创建对象（实体），你定义了类，是不是？
而在python中，类也是对象，这样的对象就是通过元类来创建的。元类就是"类的类"。
文中提到的type事实上就是一个元类，在python中，所有的类都是使用type创建的。
'''
import collections

class order_attributes(type):
    @classmethod
    def __prepare__(metacls, name, bases,**kwds):
        return collections.OrderedDict()
    def __new__(cls,name, bases,namespace):
        result=super().__new__(cls,name,bases,namespace)
        result._order = tuple(n for n in namespace if not n.startswith('_'))
        return result

class order_preserved(metaclass=order_attributes):
    pass

class something(order_preserved):
    this='text'
    def z(self):
        return False
    b='order is preserved'
    a='more text'

print(something._order)

anything=type('anything',(order_preserved,),{'a':'aa' })
print(anything._order)
print(anything.__class__)
print(anything.__class__.__class__)