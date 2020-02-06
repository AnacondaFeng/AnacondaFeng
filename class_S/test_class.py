
class Cat(object): #继承object
    """
    猫科动物类
    """
    # 类的属性
    tag = 'Cat Base'

    def __init__(self):
        # 实例化的属性
        pass

    def eat(self):
        """
        吃
        :return:
        """
        pass

    # 析构函数 一般不需要写，交给python解释器
    def __del__(self):
        pass

class Tiger(Cat):
    pass
