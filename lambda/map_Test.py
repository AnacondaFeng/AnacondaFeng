def pow_number(l):
    """
    根据给定的列表数据，计算里面每一项立方
    :param l: 列表或元组
    :return: 原来列表中每一项的立方
    """
    # 简单实现
    rest_list = []
    for x in l:
        rest_list.append(x * x * x)
    return rest_list


def f(n):
    """
    求给定数的立方
    :param n:
    :return:
    """
    return n * n * n


def pow_num_use_map(l):
    """
    使用map函数计算每一项立方
    :param l:
    :return:
    """
    return map(f, l)


def pow_num_use_map_lambda(l):
    """
    使用lambda更简单
    :param l:
    :return:
    """
    return map(lambda n: n * n * n, l)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7]
    rest = pow_number(l)
    print(rest)

    print('---------------------------')
    rest_map = pow_num_use_map(l)
    print(list(rest_map))

    print('---------------------------')
    rest_map_lambda = pow_num_use_map_lambda(l)
    print(list(rest_map_lambda))