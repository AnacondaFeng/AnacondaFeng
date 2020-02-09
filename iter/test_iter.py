
class PowNumber(object):
    """
    迭代器的实现，实现数字的平方
    """

    value = 0

    def __next__(self):
        self.value += 1

        # 这是一个新的知识点，需要特别注意！
        if self.value > 10:
            raise StopIteration
        return self.value * self.value

    def __iter__(self):
        return self

if __name__ == '__main__':
    pow = PowNumber()
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())
    # 循环迭代器
    for i in pow:
        print(pow.__next__())