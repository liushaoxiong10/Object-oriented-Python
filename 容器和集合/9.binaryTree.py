import weakref
from collections import abc

class TreeNode:
    def __init__(self, item, less=None, more=None, parent=None):
        self.item = item
        self.less = less
        self.more = more
        if parent != None:
            self.parnet = parent

    @property
    def parent(self):
        return self.parent_ref()
    @parent.setter
    def parent(self,value):
        self.parent_ref = weakref.ref(value)

    def __repr__(self):
        return ("TreeNode({item!r},{less!r},{more!r})".format(**self.__dict__))

    def find(self,item):
        if self.item is None:
            if self.more: return self.more.find(item)
        elif self.item == item : return self
        elif self.item > item and self.less:
            return self.less.find(item)
        elif self.item < item and self.more:
            return self.more.find(item)
        raise KeyError
    def __iter__(self):
        if self.less:
            for item in iter(self.less):
                yield item
        yield self.item
        if self.more:
            for item in iter(self.more):
                yield item
    def add(self,item):
        if self.item is None:
            if self.more:
                self.more.add(item)
            else:
                self.more = TreeNode(item, parent=self)
        elif self.item >= item:
            if self.less:
                self.less.add(item)
            else:
                self.less = TreeNode(item,parent=self)
        elif self.item < item:
            if self.more:
                self.more.add(item)
            else:
                self.more = TreeNode(item,parent=self)
    def remove(self,item):
        if self.item is None or item > self.item:
            if self.more:
                self.more.remove(item)
            else:
                raise KeyError
        elif item < self.item:
            if self.less:
                self.less.remove(item)
            else:
                raise KeyError
        else:
            if self.less and self.more:
                successor =self.more._least()
                self.item = successor.item
                successor.remove(successor.item)
            elif self.less:
                self._replace(self.less)
            elif self.more:
                self._replace(self.more)
            else:
                self._replace(None)

    def _least(self):
        if self.less is None: return self
        return self.less._least()
    def _replace(self,new=None):
        if self.parent:
            if self == self.parent.less:
                self.parent.less = new
            else:
                self.parent.more = new
        if new is not None :
            new.parent = self.parent

class Tree(abc.MutableSet):
    def __init__(self,iterable=None):
        self.root = TreeNode(None)
        self.size = 0
        if iterable:
            for item in iterable:
                self.root.add(item)
    def add(self, value):
        self.root.add(value)
        self.size += 1
    def discard(self, value):
        try:
            self.root.more.remove(value)
            self.size -= 1
        except KeyError:
            pass

    def __contains__(self, item):
        try:
            self.root.more.find(item)
            return True
        except KeyError:
            return False
    def __iter__(self):
        for item in iter(self.root.more):
            yield item
    def __len__(self):
        return self.size

t1=Tree(["id","name","password"])
print(list(t1))
t2=Tree(["time","IP"])
print(list(t1|t2))
t1.add("local")
print(list(t1))
if "id" in t1:
    print("True")