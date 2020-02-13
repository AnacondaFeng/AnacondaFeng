class ShortInputException(Exception):

    """自定义异常类"""

    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

    def __str__(self):
        return "这个返回的值是直接给到Result的"



if __name__ == '__main__':

    try:
        text = 'abc'
        if len(text) < 5:
            """raise直接执行异常"""
            raise ShortInputException(len(text),5)

    except ShortInputException as result:
        print("输入长度{0}，至少应该：{1}".format(result.length, result.atleast))
        print(result)


    else:
        print("无异常")

    finally:
        print("输入字符串{0}".format(text))