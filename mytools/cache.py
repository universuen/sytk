import functools


class _Cache:
    cache = dict()

    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        arg_key = f'{self.func.__name__}-{args}-{kwargs}'
        if arg_key in self.cache.keys():
            return self.cache[arg_key]
        else:
            result = self.func(*args, **kwargs)
            self.cache[arg_key] = result
            return result


cache = _Cache
