'''
当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法。在python中，对于开发者来说很少会直接销毁对象(如果需要，
应该使用del关键字销毁)。Python的内存管理机制能够很好的胜任这份工作。
不管是手动调用del还是由python自动回收都会触发__del__方法执行
'''

import time
import gc

class Animal(object):
    def __init__(self,name):
        print('__init__ 声明')
        self.name=name
    def __del__(self):
        print("__del__方法被调用")
        print("当前对象{0}被删除".format(self.name))

dog=Animal("dog")
cat=Animal("cat")
dog1=dog
cat1=cat

gc.collect()
del dog
print("Over")

