class tracer1:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer1      #spam = tracer(spam)
def spam1(a, b, c):
    print(a + b + c)

spam1(1,2,3)


class tracer2:
    def __init__(self, *args):
        self.calls = 0
        self.args = args

    def __call__(self, func):
        self.func = func
        def realfunc(*args):
            self.calls += 1
            print('call %s to %s' % (self.calls, self.func.__name__))
            print(self.args,str(args))
            self.func(*args)
        return realfunc


@tracer2("xxxx")
def spam2(a, b, c):
    print(a + b + c)

spam2(1, 2, 3)