
class MyException(Exception):
    """自定义异常类"""

    pass


def v_for():
    for i in range(1,20):
        if i == 10:
            raise MyException
        print(i)


def call_v_for():
    print('Start')
    try:
        v_for()
    except MyException() as err:
        print(err)
    print('End')

def test_raise():
    print('test start')

    call_v_for()
    # print(err)
    print('test end')

if __name__ == '__main__':
    test_raise()