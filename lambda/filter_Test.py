def use_filter(l):
    """
    获取指定列表/元组中的奇数
    :param l: list/tuple要过滤的数据
    :return: 过滤好的奇数列表
    """

    rest = filter(lambda n: n % 2 != 0, l)
    return rest


if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,0]
    print(use_filter(l))
    print(list(use_filter(l)))

