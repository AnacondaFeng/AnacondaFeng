class Cat(object):
    """
    猫科动物类
    """

    tag = '我是家猫'

    def __init__(self, name, age, sex=None):
        self.name = name
        self.__age = age  # 私有变量
        self.sex = sex

    def set_age(self, age):
        """
        改变猫的年龄
        :param age: int 年龄
        :return:
        """
        self.__age = age
        return self.__age

    def show_info(self):
        """
        显示猫的信息
        :return:
        """
        rest = '我叫：{}，今年：{}岁'.format(self.name, self.__age)
        print(rest)
        return rest

    def eat(self):
        """ 吃的方法"""
        print("猫喜欢吃鱼")

    def catch(self):
        """猫捉老鼠"""
        print('我能捉老鼠')


if __name__ == '__main__':
    # 实例化
    cat_black = Cat('小黑', 2)
    cat_black.show_info()

    print(cat_black.name)
    cat_black.name = '嘿嘿'  # 可以直接改变
    cat_black.show_info()
    # 私有变量无法直接改变
    cat_black.set_age(12)
    cat_black.show_info()

    print(Cat.tag)
    print(cat_black.tag)

    # 实例化小白
    print('*******************************')
    cat_white = Cat('小白', 3, '母的')
    cat_white.show_info()

    # 类的实例判断
    print(isinstance(cat_black, Cat))
    print(isinstance(cat_white, Cat))

