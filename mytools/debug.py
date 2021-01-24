import functools

# TODO: Fix multi-process
trigger = False


def debug(func):
    functools.wraps(func)

    def wrapper(*args, **kwargs):
        global trigger
        # if debugging trigger is in use, just wait.
        while trigger is True:
            pass
        trigger = True
        print(f'\033[1;35m[{func.__name__}]\033[0;m '
              f'\033[0;35mParams: {args, kwargs}\033[0;m')
        result = func(*args, **kwargs)
        print(f'\033[1;35m[{func.__name__}]\033[0;m '
              f'\033[0;35mReturn: {result}\n\n\033[0;m')
        trigger = False
        return result

    return wrapper


def d_print(*args, **kwargs):
    if trigger is True:
        print(f'\033[32m', end='')
        print(*args, **kwargs, end='')
        print(f'\033[0;m')


if __name__ == '__main__':
    @debug
    def test(*args):
        for i in args:
            print(i)
            d_print(f'debug_{i}')


    print(trigger)
    test(1, 2, 3)
    print(trigger)
