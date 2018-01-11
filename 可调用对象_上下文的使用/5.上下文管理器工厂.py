'''
执行 contextor 以获取上下文管理器
加载上下文管理器的 exit() 方法以备稍后调用
调用上下文管理器的 enter() 方法
如果有 as var 从句，则将 enter() 方法的返回值赋给 var
执行子代码块 with_body
调用上下文管理器的 exit() 方法，如果 with_body 的退出是由异常引发的，那么该异常的 type、value 和 traceback 会作为参数传给 exit()，否则传三个 None
如果 with_body 的退出由异常引发，并且 exit() 的返回值等于 False，那么这个异常将被重新引发一次；如果 exit() 的返回值等于 True，那么这个异常就被无视掉，继续执行后面的代码
'''

'''
希望相保存应用程序正在写的一个文件的副本
目的是将源文件重命名为filename copy 并备份
如果上下文一切正常，就删除备份文件或重命名为filename old
'''

import os

class Updating:
    def __init__(self,filename):
        self.filename=filename
    def __enter__(self):
        try:
            self.previous=self.filename+" copy"
            os.rename(self.filename,self.previous)
        except FileNotFoundError:
            self.previous=None
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            try:
                os.rename(self.filename,self.filename+" error")
            except FileNotFoundError:
                pass
            if self.previous:
                os.rename(self.previous,self.filename)

with Updating("file"):
    with open("file","w") as f:
        f.write("hellopy")
