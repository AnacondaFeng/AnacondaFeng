class Point(object):

    # 自定义Point类的构造(初始化)方法
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 自定义Point类对象的格式化输出函数(string())
    def string(self):
        print("{{X:{0}, Y:{1}}}".format(self.x, self.y), end='')


class Circle(Point):
    # 自定义Circle类的构造(初始化)方法
    def __init__(self, x, y, radius):
        # 可以简化 super().__init__(x, y)
        super(Circle, self).__init__(x, y)
        self.radius = radius

    # 自定义Circle类对象的格式化输出函数(string())
    def string(self):
        # 大括号转义的使用{{ }}
        print("该图形初始化点为:{{X:{0}, Y:{1}}} ; {{半径为:{2}}}".format(self.x, self.y, self.radius))


class Size(object):

    # 自定义Size类的构造(初始化)方法
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 自定义Size类对象的格式化输出函数(string())
    def string(self):
        print("{{Width:{0}, Height:{1}}}".format(self.width, self.height))


class Rectangle(Point, Size):

    # 自定义Rectangle类的构造(初始化)方法，并在方法中调用父类的初始化方法以完成初始化
    def __init__(self, x, y, width, height):
        # super(Rectangle, self).__init__()
        # 多重继承调用方法的使用，不用super
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)

    # 自定义Rectangle类对象的格式化输出函数(string())
    def string(self):
        # print("该图形初始化点为：{{X:{0}, Y:{1}}}; 长宽分别为:{{Width:{2}, Height:{3}}}".format(self.x, self.y, self.width,
        #                                                                           self.height))
        print("该图形初始化点为：", end='')
        Point.string(self)
        print("长宽分别为：", end='')
        Size.string(self)


if __name__ == "__main__":
    # 实例化Circle对象，圆心为（5,5），半径为8
    c = Circle(5, 5, 8)
    # 实例化Rectangle对象，顶点位置（15,15），长和宽分别为15和15
    r1 = Rectangle(15, 15, 15, 15)
    # 实例化Rectangle对象，顶点位置（40,30），长和宽分别为11和14
    r2 = Rectangle(40, 30, 11, 14)

    c.string()
    r1.string()
    r2.string()
