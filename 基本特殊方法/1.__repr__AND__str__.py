'''
__repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。
打印操作会首先尝试__str__和str内置函数(print运行的内部等价形式)，它通常应该返回一个友好的显示。
__repr__用于所有其他的环境中：用于交互模式下提示回应以及repr函数，如果没有使用__str__，会使用print和str。它通常应该返回一个编码字符串，可以用来重新创建对象，或者给开发者详细的显示。
'''
class test:
    def __init__(self,value):
        self.value=value

    def __repr__(self):
        print ("This is __repr__ "+ self.value)
    def __str__(self):
        return ("This is __str__ "+self.value)

t=test("hello")
t
print(t)