from functools import reduce


def get_sum(l):
    """
    根据给定列表，求总和
    :param l: list/ type int
    :return: 列表所有项的和
    """
    rest = 0
    for i in l:
        rest += i
    return rest


def get_sum_use_py(l):
    """
    使用python内置sum
    :param l:
    :return:
    """
    return sum(l)


def f(m, n):
    return m + n


def get_sum_use_reduce(l):
    """
    使用reduce进行求和
    :param l:
    :return:
    """
    return reduce(f, l)


def get_sum_use_reduce_lambda(l):
    """
    使用reduce进行求和lambda
    :param l:
    :return:
    """
    return reduce(lambda m, n: m + n, l)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    rest = get_sum(l)
    print(rest)

    print(get_sum_use_py(l))
    print(get_sum_use_reduce(l))
    print(get_sum_use_reduce_lambda(l))
