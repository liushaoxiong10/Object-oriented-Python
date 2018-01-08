'''
抽象基类的特性：
    1.提供一些方法定义
    2.基类意味着其他类会把它当作基类使用
    3.抽象类本身提供了一些方法的定义。抽象基类为缺失的方法函数提供了方法签名，子类必须提供正确的方法来创建符合抽象类定义的接口的具体类

考虑使用抽象基类的情况：
    1.当我们自定义类时，使用抽象基类最为基类。
    2.我们在一个方法中使用抽象基类来确保一种操作时可行的。
    3.我们在诊断信息或者异常中使用抽象基类来指出一种操作为什么不能生效。

'''

import collections.abc
#第一种情况
#SomeApplicationClasss定义为一个Callable类
class SomeApplicationClasss(collections.abc.Callable):
    pass

#第二种情况
#some_method()方法要求other参数是Iterator的一个子类，如果other参数无法通过这个测试，则会得到一个异常
class Two:
    def some_method(self,other):
        assert isinstance(other,collections.abc.Iterator)

#第三种情况可以使用以下代码判断
import warnings
def test(some_obj,another):
    try:
        some_obj.some_method(another)
    except AttributeError:
        warnings.warn("{0!r} not an Iterator, found {0.__class__.__bases__!r}".format(another))
        raise
