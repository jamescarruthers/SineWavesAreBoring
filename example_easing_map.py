import matplotlib.pyplot as plt
from numpy import arange

from easing import *

# compare different easing functions
# using an alternative way of supplying values, similar to map or interpolation functions
# ease_map(currentVal, startVal, endVal, startValue, endValue, easingFunction)

compare = [ease_in_out_cubic, ease_in_circ, ease_in_out_back]

res = 0.01

for func in compare:
    xy = []
    for x in arange(-50, 150 + res, res):
        xy.append((x, ease_map(x, 0, 100, 0, 100, func)))
    x, y = zip(*xy)
    plt.plot(x, y, label=func.__name__)

plt.gca().set_aspect('equal', adjustable='box')

# Add a legend
plt.legend()

# Display the plot
plt.show()
