from mytools import *


@cache
@debug
def test_func(*args):
    for i in args:
        d_print(i)


if __name__ == '__main__':
    t_dic = {
        '123': 456,
    }
    print(t_dic.get("666"))