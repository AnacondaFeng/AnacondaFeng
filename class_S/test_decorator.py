def log(func):
    """记录函数执行的日志"""
    """装饰器返回函数"""
    def wrapper():
        print('开始执行')
        func()
        print('执行完毕')

    return wrapper


@log
def hello():
    """
    简单功能模拟
    :return:
    """
    print("hello world")


def hello_wrapper():
    print("Start")
    hello()
    print("End")


if __name__ == '__main__':
    hello()
