def read_file():
    """
    读取文件
    :return:
    """
    file_name = "test.txt"
    # 使用绝对路径
    file_path = 'D:\\SourceCode\\Python\\AnacondaFeng\\file\\test.txt'

    # 普通方式
    f = open(file_name, encoding='utf-8')

    # rest = f.read()
    # print(rest)

    # 读取指定几个内容
    rest = f.read(8)
    # print(rest)
    # print(f.read(8))

    # 随机读取
    f.seek(20)
    # print(f.read(5))

    # 按行读取
    rest = f.readline(8)
    # print(rest)
    # print(f.readline())
    # print(f.readline())

    # 读取所有行
    rest = f.readlines()
    print(rest)

    for i in rest:
        print(i)

    f.close()

    '''
    先进模式
    '''
    #     with open
    with open(file_name, encoding='utf-8')as f:
        rest = f.readlines()
        print(rest)


if __name__ == '__main__':
    read_file()
