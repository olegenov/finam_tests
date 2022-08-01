import functools
from time import sleep


def wait(delay=3):
    def deco(func, *args):
        @functools.wraps(func)
        def inner(args, **kwargs):
            sleep(delay)
            return func(args, **kwargs)
        return inner
    return deco
