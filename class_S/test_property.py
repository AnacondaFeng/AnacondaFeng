

class PetCat(object):

    def __init__(self, name, age):

        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    # 不知道setter是干啥的
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print("error")
            return 0
        if value < 0 or value > 100:
            print("error")
            return 0
        self.__age = value

    # 描述符
    @property
    def show_info(self):

        return '我叫{0}，今年{1}岁'.format(self.name, self.age)\

    # 类的描述
    def __str__(self):
        return '{0}'.format(self.name)

if __name__=='__main__':

    cat_black = PetCat('小黑',2)
    # rest = cat_black.show_info()
    # print(rest)
    # 另外利于调试定义__str__
    print(cat_black)

    cat_black.age = 5

    # 希望不用方法，用属性反馈
    rest = cat_black.show_info
    print(rest)