#!/usr/bin/env python

from memodict import memoized
import timeit


# Simply apply the decorator to a function:
@memoized
def factoriala(n):
    return 1 if n == 1 else n * factorial(n-1) 

# ...and call it a million times:
t = timeit.Timer(lambda: factorial(30)).timeit(number=1000000)
print "Factorial: {}s\n".format(t)



# For a direct comparison:
def fib(n):
    return n if n in (0, 1) else fib(n-1) + fib(n-2)

def test(n=30):
    print "fib({}) =".format(n), fib(n)


print "Fibonacci:"

t1 = timeit.Timer(test).timeit(number=10)
fib = memoized(fib) # Decorators can also be applied like this
t2 = timeit.Timer(test).timeit(number=10)

print "cacheless: {}s".format(t1)
print "memoized:  {}s".format(t2)


