#使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用
#classmethod必须具有对类对象的引用作为第一个参数，而staticmethod根本没有参数。
#@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
#@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。


class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999
    def display(self):
        return (str(self.year)+str(self.month)+str(self.day))

date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')
print(date2.display())
print(is_date)