'''
修饰符类至少实现一个方法：
    1.Descriptor.__get__(self,instance,owner)->object : instance参数来自被访问对象的self变量。owner变量是拥有着类的对象。若在类
      中调用，instance参数默认值将为None，此方法负责返回修饰符的值
    2.Descriptor.__set__(self,instance,value) : instance参数是被访问对象的self变量，而value参数为即将赋的新值
    3.Descriptor.__delete(self,instance) : instance 参数是被访问对象的self变量，并在这个方法中实现属性值的删除。
非数据修饰符：需要定义__set__()或__delete()或两者皆有，但不能定义__get__().
            通常用于构建一些复杂表达式的逻辑
            一个不可变的非数据修饰符必须实现__set__()，而逻辑只是单纯的抛出AttributeError异常
数据修饰符：至少要定义__get__()。通常可以通过定义__get__()和__set__()函数来创建一个可变对象。这类修饰符不能定义自己内部的属性或方法，
          因为它通常是不可见得。

设计修饰符的场景：
1.修饰符对象包含或获取数据：修饰符对象的self变量是相关的并且修饰符是有状态的。
                         数据修饰符 __get__()方法返回内部数据
                         非数据修饰符  由修饰符中其他方法或属性提供数据
2.拥有者类实例包含数据：修饰符对象必须使用instance参数获取拥有者对象中的数据
                     数据修饰符  __get__()函数从实例中获取数据
                     非数据修饰符  由修饰符中其他方法提供数据
3.拥有者类包含数据：修饰符对象必须使用owner参数，由修饰符实现的静态方法或类方法的作用范围通常是全局的
'''

#非数据修饰符
class UnitValue:
    def __init__(self,unit):
        self.value=None
        self.unit=unit
        self.default_format="5.4f"
    def __set__(self, instance, value):
        self.value=value
    def __str__(self):
        return "{value:<{spec}} {unit}".format(spec=self.default_format,**self.__dict__)
    def __format__(self, spec="5.2f"):
        if spec == "":spec = self.default_format
        return "{value:{spec}} {unit}".format(spec=spec,**self.__dict__)
a=UnitValue(1)
a.value=123
print(a)
class RTD:
    rate = UnitValue("kt")      #速度
    time = UnitValue("hr")      #时间
    distance = UnitValue("nm")  #距离
    def __init__(self,rate=None,time=None,distance=None):
        if rate is None:
            self.time = time
            self.distance = distance
            self.rate = distance / time
        if time is None:
            self.rate = rate
            self.distance = distance
            self.time = distance/rate
        if distance is None:
            self.rate = rate
            self.time = time
            self.distance = rate*time
    def __str__(self):
        return "rate: {0.rate} time: {0.time} distance: {0.distance}".format(self)

m=RTD(rate=5.8,distance=12)
print(m)

#数据修饰符
class Unit:
    conversion=1.0
    def __get__(self, instance, owner):
        return instance.kph * self.conversion
    def __set__(self, instance, value):
        instance.kph = value/self.conversion
    #kph(千米每小时)
class Knots(Unit):
    conversion = 0.599568

class Mph(Unit):
    conversion = 0.62137119

class KPH(Unit):
    def __get__(self, instance, owner):
        return instance._kph
    def __set__(self, instance, value):
        instance._kph = value



class Measurement:
    kph = KPH()
    knots = Knots()
    mph = Mph()
    def __init__(self,kph=None,mph=None,knots=None):
        if kph: self.kph = kph
        elif mph: self.mph = mph
        elif knots: self.knots = knots
        else:
            raise TypeError
    def __str__(self):
        return "rate : {0.kph} kph = {0.mph} mph = {0.knots} knots".format(self)

m=Measurement(knots=5.9)
print(m)