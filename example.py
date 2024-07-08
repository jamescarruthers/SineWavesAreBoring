import matplotlib.pyplot as plt
from numpy import arange

from easing import *

# compare different easing functions as waves

compare = [ease_in_out_cubic, ease_in_circ, ease_in_out_back]

res = 0.01

for func in compare:
    xy = []
    for x in arange(-2, 2 + res, res):
        xy.append((x, wave(x, func)))
    x, y = zip(*xy)
    plt.plot(x, y, linestyle='-', label=func.__name__)

plt.gca().set_aspect('equal', adjustable='box')

# Add a legend
plt.legend()

# Display the plot
plt.show()
