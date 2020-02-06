class BaseCat(object):
    """
    猫科动物的基础类
    """
    tag = '猫科动物'

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("猫都要吃东西")


# 多重继承
class ProtectedMixin(object):

    def protected(self):
        print("我是受保护的")


class Tiger(BaseCat, ProtectedMixin):
    """
    老虎类 继承猫科动物
    """

    def eat(self):
        super(Tiger, self).eat()
        print("我还喜欢吃肉，大猪肉")


class Panda(BaseCat, ProtectedMixin):
    """
    熊猫类 继承猫科动物
    """
    pass


class PetCat(BaseCat):
    """
    家猫类 继承猫科动物
    """

    def eat(self):
        super(PetCat, self).eat()
        print("我还喜欢吃猫粮")


class HuaCat(PetCat):
    """
    中华田园猫
    """

    def eat(self):
        super(HuaCat, self).eat()
        print("我还喜欢吃零食")


class DuanCat(PetCat):
    """
    英短
    """
    pass


if __name__ == '__main__':
    # # 实例化中华田园猫
    # cat = HuaCat('小黄')
    # cat.eat()
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # cat_d = DuanCat('小辉')
    # cat_d.eat()
    #
    # # 子类判断
    # print(issubclass(DuanCat, BaseCat))

    panda = Panda('little')
    panda.eat()
    panda.protected()

    tiger = Tiger('Big')
    tiger.eat()
    tiger.protected()

    # 多重继承，有相同方法的基类，先执行第一个，后面不执行
