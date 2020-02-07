class Car(object):
    # Car类的基本车型设置，列表形式
    description = ['大众', '丰田', '广本', '沃尔沃', '凯迪拉克']

    # 重写该类的构造方法，并将参数l、w、h、brand赋值给实例对象属性
    def __init__(self, l, w, h, brand):
        self.L = l
        self.W = w
        self.H = h
        self.brand = brand

    # 自定义该类的基本车型检索方法
    def modify_des(self):
        if self.brand in self.description:
            return self.brand
        else:
            return '请输入您的车辆描述'

    # 自定义静态方法 提示用户：‘已完成车辆基本参数信息的录入！’
    @staticmethod
    def basic_parameters():
        print("已完成车辆基本参数信息的录入！")

    # 自定义类方法 根据用户车辆的品牌给出相应的合理保养建议
    @classmethod
    def unkeep(cls, desc):
        if desc in cls.description:
            print("根据汽车保养的相关经验，{0}品牌的车应于5000km/次的频率进行专业性保养".format(desc))
        else:
            print("非常抱歉！{0}品牌不在我们的保养范围内".format(desc))


if __name__ == '__main__':
    car_1 = Car(4.2, 1.8, 1.5, '大众')

    # 调用实例方法：basic_parameters（）
    # car_1.basic_parameters()
    Car.basic_parameters()
    # 利用if语句，调用modify_des()以判断Car的类属性description是否存在
    des_rest = car_1.modify_des()
    if des_rest != '请输入您的车辆描述':
        car_1.unkeep(des_rest)
    else:
        print(des_rest)
    # 若if判断条件成立 则调用类方法upkeep（）并将对应实例的brand属性传递给参数desc

    # 当if语句的判断条件不成立时，打印输出并提示用户：‘请正确填写相关的车辆信息’

    car_2 = Car(4.2, 1.8, 1.5, '保时捷')

    # 调用实例方法：basic_parameters（）
    Car.basic_parameters()

    # 利用if语句，调用modify_des()以判断Car的类属性description是否存在
    des_rest = car_2.modify_des()
    if des_rest != '请输入您的车辆描述':
        car_2.unkeep(des_rest)
    else:
        print(des_rest)
    # 若if判断条件成立，则调用类方法upkeep（）并将对应实例的brand属性传递给参数desc

    # 当if语句的判断条件不成立时，打印输出并提示用户：‘请正确填写相关的车辆信息’
