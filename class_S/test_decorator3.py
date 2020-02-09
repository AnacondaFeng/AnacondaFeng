
# 带参数的装饰器
def log(name=None):
    def decorator(func):
        def wrapper():
            print('{0}.start..'.format(name))
            func()
            print('{0}.end..'.format(name))
        return wrapper
    return decorator

# 执行方法带参数的装饰器
def log2(name=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('{0}.start..'.format(name))
            rest = func(*args, **kwargs)
            print('{0}.end..'.format(name))
            return rest
        return wrapper
    return decorator

@log('you')
def hello():
    """
    简单功能模拟
    :return:
    """
    print("hello world")

@log2('test')
def add(a,b):
    return a+b

if __name__ == '__main__':
    hello()

    rest = add(5,6)
    print(rest)
