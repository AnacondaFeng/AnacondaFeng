
def test_div(num1, num2):
    """除数为0"""
    return num1/num2

if __name__ == '__main__':
    # try:
    #     rest = test_div(5,0)
    #     print(rest)
    # except:
    #     print('报错了')

    try:
        rest = test_div('a',0)
        print(rest)
    except ZeroDivisionError:
        print('报错了,1')
    except TypeError:
        print('报错了,2')

    except(ZeroDivisionError, TypeError):
        print('报错了，1+2')

    except(ZeroDivisionError, TypeError) as err:
        print(err)

    finally:
        print('必须要执行的')