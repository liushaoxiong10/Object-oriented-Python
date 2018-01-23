'''
ChainMap是python3的新特性，它用来将多个map组成一个新的单元（原来的map结构仍然存在，类似于这些map被存在了一个list之中），这比新建一个
map再将其他map用update加进来快得多。通过ChainMap可以来模拟嵌套的情景，而且多用于模板之中。

可以传入多个map来初始化ChainMap，如参数为空，会自动加入一个空的map
获取的key如果不存在，则返回None
获取key根据顺序获取
可以通过new_child()方法来新增map，新的map添加在前面
parents属性返回除去第一个map后的ChainMap实例。
'''
from collections import  ChainMap

a={"first":1,"sec":2}
b={"bb":3,"first":4}
c=ChainMap(a,b)
print(c)
print(c.get("first"))
print(c.items())
print(c.keys())
print(c.values())
for i in c.values():
    print(i)
d={"ddd":9}
c=c.new_child(d)
print(c.items())
