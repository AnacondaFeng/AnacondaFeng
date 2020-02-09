def use_range():
    for i in range(5, 10):
        print(i)


# 使用迭代器

class IterRange(object):
    """使用迭代器模拟Range"""

    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


# 使用生成器

class GenRange(object):
    """使用生成器模拟Range"""

    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def get_num(self):
        while True:
            if self.start >= self.end - 1:
                break
            self.start += 1
            yield self.start


if __name__ == '__main__':
    # use_range()
    #
    # iter = IterRange(5, 10)
    # print(next(iter))
    #
    # l = list(iter)
    # print(l)

    gen = GenRange(5, 10).get_num()
    print(list(gen))
