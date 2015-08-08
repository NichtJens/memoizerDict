
from functools import update_wrapper


class memoized(dict):
    """
    Decorator to add a cache to a function, based on dict
    using its built-in fallback for missing elements
    Does NOT support functions with kwargs
    """

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args):
        """Build a key, return dict item for that key"""
        self.args = args
        return self[args]

    def __missing__(self, key):
        """Is called for missing keys, calculates and stores them"""
        self[key] = self.func(*self.args)
        return self[key]

    @property
    def cache(self):
        return [(x, y) for x, y in sorted(self.items())]


