class Explore(list):
    def __init__(self,*args, **kw):
        self.sum0 = 0
        self.sum1 = 0
        self.sum2 = 0
        super().__init__(*args, ** kw)
        for x in self:
            self._new(x)
    def __getitem__(self, item):
        if isinstance(item,slice):
            print(item,item.indices(len(self)))
            return super().__getitem__(item)
        else:
            return super().__getitem__(item)

    def _new(self,value):
         self.sum0 += 1
         self.sum1 += value
         self.sum2 += value*value


    def _rmv(self,value):
        self.sum0 -= 1
        self.sum1 -= value
        self.sum2 -= value*value

    def insert(self, index, value):
        super().insert(index,value)
        self._new(value)
    def pop(self, index = 0):
        value = super().pop(index)
        self._rmv(value)
        return value

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            olds = [self[i] for i in range(start,stop,step)]
            super().__setitem__(key,value)
            for x in olds:
                self._rmv(x)
            for x in value:
                self._new(x)
        else:
            old = self[key]
            super().__setitem__(key,value)
            self._rmv(old)
            self._new(value)
    def __delitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            olds = [self[i] for i in range(start,stop,step)]
            super().__delitem__(key)
            for x in olds:
                self._rmv(x)
        else:
            old = self[key]
            super().__delitem__(key)
            self._rmv(old)
    def display(self):
        print(self)
        print(str(self.sum0)+'_'+str(self.sum1)+'_'+str(self.sum2))

a=Explore([1,2,3,4,5])
a.display()
print(a[:2])
print(a[2])
a[1]=3
a.display()
a.insert(1,2)
a.display()
a.__delitem__(2)
a.display()

