# import django

# import pay
# from pay.alipay import tools as alipay
# from pay.wechat_pay import tools as wepay

from chapter01.pay.alipay.tools import pay as alipay
from chapter01.pay.wechat_pay.tools import pay as wepay


# import 顺序
# 1.标准库
# 2.第三方库包
# 3.自定义包/模块


# PEP8
def funct():
    """局部import"""


def fun2():
    # tools.pay()
    pass


def fun3():
    alipay()
    wepay()


if __name__ == '__main__':
    fun3()
