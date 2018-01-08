'''
创建新属性
为现有属性赋值
获取属性的值
删除属性
'''

class Generic:
    string="gra"
    pass
g=Generic()

g.attr="value"
print(g.attr)
print(g.string)
g.string="g"
print(g.string)
del g.attr
