import matplotlib.pyplot as plt
from numpy import arange

from waves import *

# compare different wave functions
# wave returns -1 to 1, the input 
# wave(x, easingFunction)

compare = [ease_in_out_cubic, ease_in_out_circ, ease_in_out_back]

res = 0.01

for func in compare:
    xy = []
    for x in arange(-1, 1 + res, res):
        xy.append((x, wave(x, func)))
    x, y = zip(*xy)
    plt.plot(x, y, label=func.__name__)

plt.gca().set_aspect('equal')

# Add a legend
plt.legend()

# Display the plot
plt.show()
