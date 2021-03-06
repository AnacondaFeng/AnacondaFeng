# 从functools 中导入reduce函数
from functools import reduce

def use_reduce(data):
    # 使用result接收reduce实现20的阶乘
    result = reduce(lambda m, n: m * n, data)
    print(result)


# 测试该功能
if __name__ == '__main__':
    # 使用data接收一个1-20的数值
    data = list(range(1, 21))
    # 调用use_reduce函数传入data
    use_reduce(data)
