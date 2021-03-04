from sytk import timer
from time import sleep


@timer
def test():
    sleep(1)


if __name__ == '__main__':
    test()
