def eat(cls):
    cls.eat = lambda self: print('{0}>我要吃东西'.format(self.name))
    return cls


def f(self):
    print('{0}>我要吃东西'.format(self.name))
    print('000000000000000000000')


def eat2(cls):
    cls.eat = f
    return cls


@eat2
class Cat(object):
    """猫类"""

    def __init__(self, name):
        self.name = name


if __name__ == 'main':
    cat = Cat('小黑')
    cat.eat()
