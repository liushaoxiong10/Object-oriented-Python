'''
Container 基类要求子类实现__contains__()方法，这个方法实现了in运算符
Iterable 基类要求子类实现__iter__()方法，for语句、生成器表达式和iter()函数都需要
Sized 基类要求子类实现__len__() 方法，len()函数使用这个方法
Hashable 基类要求子类实现__hash__() 方法，hash()函数需要使用，如果这个方法被实现了那就意味着当前对象是不可变的

复合基类
Sequence 和 MutableSequence 类，基于 index()、count()、reverse()、extend()和remove()
Mapping 和 MutableMapping 类 ， 包含key()、items()、values()、get() 等
Set 和 MutableSet 类，包含用于set类型的比较操作和算数运算符的实现
'''


class A(object):
    def __init__(self, num):
        self.num = [i for i in range(num)]

    def __contains__(self, item):
        '''''
        @summary:当使用in，not in 对象的时候 ,not in 是在in完成后再取反,实际上还是in操作
        '''
        # print("__contains__:%s is in?" % item)
        # if item < self.num and item >= 0:
        #     return True
        # return False
        return any(item == i for i in self.num)

if __name__ == "__main__":
    if 3 in A(10):
        print("True")
    else:
        print("False")

    if 3 not in A(10):
        print("True")
    else:
        print("False")
