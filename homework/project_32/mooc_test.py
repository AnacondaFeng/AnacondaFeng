import random
import sys
from datetime import datetime


def guide_page(guide_word):
    """
    提示玩家进入游戏，并输出信息
    :param guide_word: 记录输出标题文字信息
    :return:
    """
    print("***************************{0}***************************".format(guide_word))


def all_num(n):
    """判断指定的值是否为数字"""
    return str(n).isdigit() == True


def num_legal(ls):
    """
    1.判定序列中数值是否相等
    2.记录数字区间起始位置值是否大于终止位置的值
    :param ls: 接收指定序列
    :return: 退出sys.exit() or 1
    """
    if int(ls[0]) == int(ls[1]):
        print("您输入的区间数字相同！！请重新启动程序")
        sys.exit()
    elif int(ls[0]) > int(ls[1]):
        print("您输入的数字区间大小有误！！请重新启动程序")
        sys.exit()
    else:
        return 1


def set_final_num(num1, num2):
    """
    自定义产生区间随机数
    1.将两个数记录到列表中
    2.判断列表中的值是不是数字
    :param num1:起始位置
    :param num2: 终止位置
    :return:
    """
    num_range = [num1, num2]

    num_range_rest = list(filter(all_num, num_range))

    # print(len(num_range_rest))

    if len(num_range_rest) == 2:
        if num_legal(num_range_rest) == 1:
            print("所产生的的随机数字区间为：{}".format(num_range_rest))
            target_num = random.randint(int(num1), int(num2) + 1)
            # print(target_num)
            return target_num
    else:
        print('您所输入的为非数字字符，请重新启动！')
        sys.exit()


def check_num_legal(num):
    """
    检查数值是否在指定区间
    :param num: 输入数值
    :return:
    """
    if num not in range(int(i), int(j) + 1):
        print("对不起您输入的数字未在指定区间！！！")
        return True
    else:
        return False


def write_record(times, value):
    """
    将猜测数字和次数写入日志文件
    数字输入时间datetime记录
    with open a追加日志文件
    :param times: 输入时间
    :param value: 输入值
    :return:
    """
    log_info = "{0}:第{1}次您猜测的数字为:{2}".format(datetime.now(), times, value)
    file_name = "record.txt"
    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(log_info)
        f.write('\n')


def main(rand1):
    """
    1.根据已产生的随机数字，记录次数
    2.设置无限循环
    :param rand1:随机数字
    :return:
    """
    times = 0
    while True:
        temp = int(input("请继续输入您猜测的数字："))
        if check_num_legal(temp):
            continue
        times += 1
        write_record(times, temp)
        # print("测试{}次".format(times))
        if rand1 > temp:
            print("Lower than the answer")
        elif rand1 < temp:
            print("Higher than the answer")
        else:
            print("恭喜您！只用了{0}次就赢得了游戏".format(times))
            break


if __name__ == '__main__':
    """
    1.guide_page()输出标题
    2.接收数字区间
    3.set_final_num()得到随机数
    4.main()执行循环
    """

    guide_page("欢迎进入数字猜猜猜小游戏")
    i = input("数字区间起始值：")
    j = input("数字区间终止值：")
    main(set_final_num(i, j))
