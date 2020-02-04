# import datetime
import random
from datetime import datetime


def write_file():
    """
    写入文件
    :return:
    """
    # 传统方式
    file_name = 'write_test.txt'
    # 以写入方式打开文件
    f = open(file_name, 'w')
    f.write('hello')
    # 换行符 \r\n
    f.write('\n')
    f.write('world')
    # 关闭文件
    f.close()


def write_mult_line():
    """
    向文件中写入多行
    :return:
    """
    file_name = 'write_mult_lines.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        l = ['line1', '\n', 'line2', '\r\n', '中文']
        f.writelines(l)


def write_user_log():
    """记录用户日志"""
    rest = '用户：{0} - 访问时间{1}'.format(random.randint(1000, 9999), datetime.now())
    # print(rest)

    file_name = 'write_user_log.txt'

    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(rest)
        f.write('\n')

def read_and_write():
    """先读再写入 用r+"""

    file_name = 'read_and_write.txt'
    with open(file_name, 'r+', encoding='utf-8') as f:
        read_rest = f.read()

        if '1' in read_rest:
            f.write('bbb')
        else:
            f.write('aaa')

        f.write('\n')

if __name__ == '__main__':
    # write_mult_line()
    # write_user_log()

    read_and_write()