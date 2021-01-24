from mytools import *


@cache
@debug
def test_func(*args):
    for i in args:
        print(i)
        d_print(i)


if __name__ == '__main__':
    test_func(1, 2, 3)