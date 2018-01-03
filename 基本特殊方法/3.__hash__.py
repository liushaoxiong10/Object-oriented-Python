'''
本函数返回对象的哈希值。
'''

test=object()
print(hash(test))
print(id(test))
print(id(test)/16)

class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __hash__(self):
        return self.a*self.b

t=test(2,3)
print(hash(t))