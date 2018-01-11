from functools import lru_cache
'''
LRU(最近最少使用)缓存
'''
@lru_cache(None)
def power(x,n):
    if n == 0: return 1
    elif n % 2 == 1:
        return pow(x,n-1)*x
    else:
        t = pow(x,n//2)
        return t*t

print(power(2,10))
print(power(2,5))