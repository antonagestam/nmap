import matplotlib.pyplot as plt
import numpy as np
import math

from lib.ease import *

x = np.linspace(0, 1)
yaxis = (np.linspace(0, 0), np.linspace(-10, 10))
fns = [cubic_in, cubic_out, cubic_in_out, out_back]
size = math.ceil(math.sqrt(len(fns)))
size = size * 100 + size * 10

for i, fn in enumerate(fns):
    plt.subplot(size + i + 1)
    plt.plot(*yaxis, 'black')
    plt.plot(*reversed(yaxis), 'black')
    plt.plot(x, np.array([fn(xn) for xn in x]))
    plt.title(fn.__name__)
    plt.axis('equal')
    plt.axis([0, 1, 0, 1.3])

plt.show()
