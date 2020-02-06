def calc(a, b, c):
    return (a + b) * c


if __name__ == '__main__':
    l = {'a': 1, 'b': 2, 'c': 5}
    print(calc(**l))
