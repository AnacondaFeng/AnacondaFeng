# import random
# print("Hello Python Hello World!!!")
#
#
# def testFunction():
#     print("welcome this function")
#     r = random.randint(1,19)
#     return r
#
# print(testFunction())

# a是生成器的写法
# a = (x for x in range(8))
# b = [x for x in range(10)]
# print(len(b))
# # print(len(a))
# print(a.__next__())
# print(a.__next__())

# try:
#     f = open('1.txt','r')
#     try:
#         content = f.read()
#         print(content)
#         f.close()
#     except NameError as err:
#         print('1')
# except FileNotFoundError as err:
#     print('2')
# else:
#     print('3')

class Imooc(object):
    __slots__ = ('name','age')

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        return 'Imooc'

def  run():
    print('run')

if __name__ == '__main__':

    imooc = Imooc('小梅',20)
    imooc.run = run
    imooc.run()
