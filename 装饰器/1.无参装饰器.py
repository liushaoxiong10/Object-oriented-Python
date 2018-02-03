import functools
import logging
import sys

def debug(function):
    @functools.wraps(function)
    def logged_function(*args , **kwargs):
        logging.debug("%s( %r, %r )", function.__name__,args, kwargs, )
        result = function(*args, **kwargs)
        logging.debug("%s = %r", function.__name__, result)
        return result
    return logged_function

@debug
def test(m, n):
    if m == n : return n+1
    elif m > 0 and n == 0 : return test(m-1, 1)
    elif m >0 and n > 0 : return test(m-1, test(m, n-1))
    else: return 2
logging.basicConfig(stream=sys.stderr, level= logging.DEBUG)  #配置日志记录器

print(test(4,2))