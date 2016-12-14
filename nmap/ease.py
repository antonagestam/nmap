import time
import math
from functools import lru_cache


def now():
    return int(round(time.time() * 1000))


def linear(n):
    return n


def cubic_in(n):
    return n ** 2


def cubic_out(n):
    return -n * (n-2)


def cubic_in_out(n):
    if n < .5:
        return 2 * n**2
    n = n * 2 - 1
    return -.5 * (n * (n - 2) - 1)


def out_back(n, s=2.70158):
    n = n - 1
    return n * n * ((s + 1) * n + s) + 1


def ease(fn, duration, from_value, to_value):
    curve = lambda t: fn(t/duration) * (to_value - from_value) 
    #curve = lru_cache(maxsize=1)(curve)
    t0 = now()

    while True:
        t = now() - t0
        if t > duration:
            break
        yield curve(t)

    while True:
        stopval = curve(t)
        yield stopval
