import functools
from mytools.debug import *


class _Cache:
    cache = dict()

    def __init__(self, func, cache_in_rom=False):
        d_print('Decorator initialized')
        d_print(f'func is {func}')
        self.func = func
        self.cache_in_rom = cache_in_rom

    @debug
    def __call__(self, *args, **kwargs):
        d_print('Decorator called')
        arg_key = f'{self.func.__name__}-{args}-{kwargs}'
        if arg_key in self.cache.keys():
            d_print(f'{arg_key} is in cache, and its result is {self.cache[arg_key]}')
            return self.cache[arg_key]
        else:
            d_print(f'{arg_key} is not in cache')
            result = self.func(*args, **kwargs)
            self.cache[arg_key] = result
            return result


# @debug
def cache(func=None, cache_in_rom=False):
    d_print(f'func is {func}')
    if func is None:
        return functools.partial(_Cache, cache_in_rom=cache_in_rom)
    else:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return _Cache(func, cache_in_rom=cache_in_rom)(*args, **kwargs)

        return wrapper


if __name__ == '__main__':
    @cache
    # @debug
    def test(*args):
        d_print('666')
        return sum(args)

    test(1, 2, 3)
    test(4, 5, 6)
    test(1, 2, 3)
