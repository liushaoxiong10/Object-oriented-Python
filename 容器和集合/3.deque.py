'''
deque 一个双向队列   为列表中的第一个和最后一个元素提供一致的性能，他的追加和弹出的效率比list对象快
'''

from collections import deque

d = deque("abcdefg")  #构建对象
print(d)
d.remove('b')    #移除元素
print(d)
d.appendleft('h')  #左侧添加
print(d)
d.append('j')   #右侧天津
print(d)
print(d.pop())   #右侧弹出
print(d)
print(d.popleft())  #左侧弹出
print(d)
d.extend("jkl")    #右侧批量添加元素
print(d)
d.extendleft("qwe")   #左侧批量添加元素
print(d)
d.reverse()   #反转
print(d)
print(d.count('e'))  #统计某元素个数
d.rotate(2)  #将队列后的若干元素移到前
print(d)
d.clear()  #清除队列
print(d)
