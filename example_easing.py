import matplotlib.pyplot as plt
from numpy import arange

from waves import *

# compare different easing functions
# using the standard style of ease
# ease(currentTime, beginValue, changeValue, duration, easingFunction)

compare = [ease_in_out_cubic, ease_in_circ, ease_in_out_back]

res = 0.01

for func in compare:
    xy = []
    for x in arange(-50, 150 + res, res):
        xy.append((x, ease(x, 0, 50, 100, func)))
    x, y = zip(*xy)
    plt.plot(x, y, label=func.__name__)

plt.gca().set_aspect('equal', adjustable='box')

# Add a legend
plt.legend()

# Display the plot
plt.show()
