# memoizerDict
A memoizer is a decorator that adds a cache to a function.
This module contains a Python implementation based on dict by using its built-in fallback for missing elements.

---

The prototypical implementation of a memoizer in Python probably looks like this:

```python
from functools import wraps

def memoized(obj):
    cache = obj.cache = {}

    @wraps(obj)
    def memoizer(*args):
        if args not in cache:
            cache[args] = obj(*args)
        return cache[args]
    return memoizer
```

... but if a dict is used as realization of the cache, why not subclass it instead?

Indeed, the `dict.__missing__()` magic method is ideal for triggering calculation via the wrapped function, so that `__call__()` becomes trivial:

```python
from functools import update_wrapper

class memoized(dict):
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        self[key] = self.func(*key)
        return self[key]
```

For the actual implementation including docstrings see [here](memodict.py).

An extended version that can deal with functions that have keyword arguments is also available [here](memodictkw.py).
