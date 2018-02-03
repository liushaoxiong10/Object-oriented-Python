import logging
import functools
import sys
def debug_named(log_name):
    def con(function):
        @functools.wraps(function)
        def wrapped(*args, ** kwargs):
            log = logging.getLogger( log_name )
            log.debug("%s( %r, %r)",function.__name__ , args,kwargs,)
            result = function(*args, ** kwargs)
            log.debug("%s = %r",function.__name__,result)
            return result
        return wrapped
    return con

@debug_named("test_name")
def test(m, n):
    if m == n : return n+1
    elif m > 0 and n == 0 : return test(m-1, 1)
    elif m >0 and n > 0 : return test(m-1, test(m, n-1))
    else: return 2
logging.basicConfig(stream=sys.stderr, level= logging.DEBUG)  #配置日志记录器

test(2,2) 