# memoizerDict
A memoizer is a decorator that adds a cache to a function.
This module contains a Python implementation based on dict by using its built-in fallback for missing elements.

---

Note that the prototypical implementation of a memoizer in Python probably looks more like this:

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


