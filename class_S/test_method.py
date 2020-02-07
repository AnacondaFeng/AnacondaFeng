class Cat(object):
    tag = '猫科动物'

    def __init__(self, name):
        self.name = name

    # 静态方法
    @staticmethod
    def breath():
        """呼吸"""
        print("猫都需要呼吸")

    # 类的方法
    @classmethod
    def show_info(cls,name):
        """显示猫的信息"""
        # print('类的属性{0}， 实例的属性{1}'.format(cls.tag, cls.name))
        # return cls(name)
        pass

if __name__ == '__main__':
    # 通过类直接调用
    Cat.breath()

    # 通过类的实例进行调用
    cat = Cat('小黑')
    cat.breath()
    cat.show_info()


    # 调用classmethod
    cat2 = Cat.show_info('小黄')
    cat2.show_info()