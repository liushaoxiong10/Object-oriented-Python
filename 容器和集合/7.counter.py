'''
Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任
意的Interger（包括0和负数）。

'''
from collections import Counter
c = Counter()  # 创建一个空的Counter类
c = Counter('gallahad')  # 从一个可iterable对象（list、tuple、dict、字符串等）创建
c = Counter({'a': 4, 'b': 2})  # 从一个字典对象创建
c = Counter(a=4, b=2)  # 从一组键值对创建

print(list(c.elements()))
'''
sum(c.values())  # 所有计数的总数
c.clear()  # 重置Counter对象，注意不是删除
list(c)  # 将c中的键转为列表
set(c)  # 将c中的键转为set
dict(c)  # 将c中的键值对转为字典
c.items()  # 转为(elem, cnt)格式的列表
Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
c.most_common()[:-n:-1]  # 取出计数最少的n-1个元素
c += Counter()  # 移除0和负值
'''

for k, j in c.most_common():
    print(k,j)