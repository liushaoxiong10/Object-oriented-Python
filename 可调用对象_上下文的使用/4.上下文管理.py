'''
使用with实现
'''
# with open("file",'r') as f:
#     f.read()
'''
上下文管理器的定义包含两个特殊方法：__enter__() 和 __exit__()
with使用它们进行上下文的进入和退出
'''
import random
class KnownSequence:
    def __init__(self,seed=0):
        self.seed=seed
    def __enter__(self):
        self.was =random.getstate()    #获取当前状态
        random.seed(self.seed,version=1)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        random.setstate(self.was)

print(tuple(random.randint(-1,36) for i in range(5)))
with KnownSequence():
    print(tuple(random.randint(-1, 36) for i in range(5)))
print(tuple(random.randint(-1,36) for i in range(5)))
with KnownSequence():
    print(tuple(random.randint(-1, 36) for i in range(5)))
print(tuple(random.randint(-1,36) for i in range(5)))


'''
每次创建一个KnownSequence的实例，修改了random模块的实现
在with语句中会得到一串固定的随机串
'''
