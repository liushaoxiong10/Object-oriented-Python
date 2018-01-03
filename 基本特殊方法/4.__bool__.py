class test:
    def __init__(self,a):
        self.a=a
    def display(self):
        for i in self.a:
            print(i)
    def pop(self):
        return (self.a.pop())
    def __bool__(self):
        return bool(self.a)

t=test([1,2,3,4,5])
t.display()
print(t.pop())
while t:
    print(t.pop())
