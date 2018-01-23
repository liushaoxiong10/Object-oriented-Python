'''
OrderDict 叫做有序字典,也是字典类型(dict)的一个子类,是对字典的一个补充。
字典类型是一个无序的集合,如需排序，我们可能会将字典的键值取出来做排序后在根据键值来进行有序的输出
OrderDict 本身就为有序字典
'''

aDict = {}
aDict["a"] = "123"
aDict["c"] = "jkl"
aDict["b"] = "234"
aDict["d"] = "iop"
for i, j in aDict.items():
    print(i+j)

from collections import OrderedDict
bDict = OrderedDict()
bDict["a"] = "123"
bDict["d"] = "aq2"
bDict["c"] = "1df"
for i, j in bDict.items():
    print(i+j)
