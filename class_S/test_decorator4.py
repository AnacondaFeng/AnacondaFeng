# 执行方法带参数的装饰器
from functools import wraps


def log2(name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """doc在这了"""
            print('{0}.start..'.format(name))
            rest = func(*args, **kwargs)
            print('{0}.end..'.format(name))
            return rest
        return wrapper
    return decorator

@log2('test')
def add(a,b):
    """这是我想看的doc"""
    return a+b

if __name__=='__main__':

    print('doc:{0}'.format(add.__doc__))