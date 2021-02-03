from sytk import *

@cache
@debug
def test_func(*args):
    d_print("You won't see this unless you decorated me with @debug.")
    print("I'm calculating data, it will take a long time.")
    print("......(long time)")
    print("Done!")
    return sum(args)


if __name__ == '__main__':
    print(test_func(1, 2, 3))
    print(test_func.__name__)
    print(test_func(7, 8, 9))
    print(test_func(1, 2, 3))
