import collections.abc

class Power1(collections.abc.Callable):
    def __call__(self, x, n):
        p = 1
        for i in range(n):
            p *= x
        return p
pow1=Power1()
print(pow1(2,0))
print(pow1(2,2))

'''
提高性能
    使用更好的算法，包含缓存
'''
#分治算法
'''
如果n=0 ： x^n =1 
如果n是奇数并且n mod 2 = 1 ，结果为x^(n-1)*n
如果n是偶数并且n mod = 0，结果为x^(n/2)*x^(n/2)

'''

class Power2(collections.abc.Callable):
    def __call__(self, x, n):
        if n == 0: return 1
        elif n % 2 == 1:
            return self.__call__(x, n-1)*x
        else:
            t = self.__call__(x,n/2)
            return t*t
power2=Power2()
print(power2(2,10))

#缓存
class Power3(collections.abc.Callable):
    def __init__(self):
        self.memo = {}
    def __call__(self, x, n ):
        if (x,n) not in self.memo:
            if n == 0:
                self.memo[x,n] = 1
            elif n % 2 == 1:
                self.memo[x,n] = self.__call__(x, n-1) * x
            elif n % 2 == 0:
                t = self.__call__(x , n //2)
                self.memo[x,n] = t*t
            else:
                raise Exception("Logic Error")
        return self.memo[x,n]

power3=Power3()
print(power3(100,100))
print(power3.memo)

