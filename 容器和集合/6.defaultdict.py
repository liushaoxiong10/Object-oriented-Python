'''
简单的dict在使用不存在的key的时候发生KeyError这样的一个报错
使用defaultdict任何未定义的key都会默认返回一个根据method_factory参数不同的默认值, 而相同情况下dict()会返回KeyError.

default_factory 接收一个工厂函数作为参数, 例如int str list set等.
defaultdict在dict的基础上添加了一个missing(key)方法, 在调用一个不存的key的时候, defaultdict会调用__missing__, 返回一个
根据default_factory参数的默认值, 所以不会返回Keyerror.
'''

from collections import defaultdict

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
  d[k].add(v)
print(d.items())
print(d['r'])