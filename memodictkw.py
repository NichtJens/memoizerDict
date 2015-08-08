
from functools import update_wrapper


class memoized(dict):
    """
    Decorator to add a cache to a function, based on dict
    using its built-in fallback for missing elements
    Supports functions with kwargs
    """

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        """Build a key, return dict item for that key"""
        self.args   = args
        self.kwargs = kwargs
        key = make_key(*args, **kwargs)
        return self[key]

    def __missing__(self, key):
        """Is called for missing keys, calculates and stores them"""
        self[key] = self.func(*self.args, **self.kwargs)
        return self[key]

    @property
    def cache(self):
        return [(x, y) for x, y in sorted(self.items())]



def make_key(*args, **kwargs):
    """Combine args and kwargs into a dict key"""
    hashable_kwargs = hashable_dict(kwargs)
    return args, hashable_kwargs


def hashable_dict(d):
    """Create a hashable object from the items of a dict"""
    # Alternative 1: sorted tuple
    # sorted() should act fine on kwargs dicts, as keys are always strings
    return tuple(sorted(d.items()))
    # Alternative 2: frozenset
    # For unorderable dicts, but then the values in kwargs need to be hashable
    return frozenset(d.items())
    # Alternative 3: string representation
    # For unhashable values, but danger of huge cache as strings might be long
    # plus overhead of hashing long strings
    return str(sorted(d.items()))


