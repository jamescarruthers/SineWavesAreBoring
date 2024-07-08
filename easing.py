import math
import numpy as np

############
# x should be a temporal dimension such as time or position
############

def wave(x, easingFunction):
    # ensure that 0 to 1 = a full wave
    x *= 2
    # ensure that the wave starts on zero
    x -= 0.5
    # modulus to repeat wave
    x = x % 2.0
    if x > 1:
        x = 2 - x
    return 2 * easingFunction(x) - 1

############
# Included easing functions for completeness
############

def ease(currentTime, beginValue, changeValue, duration, easingFunction):

    if currentTime <= 0:
        return beginValue
    elif currentTime >= duration:
        return beginValue + changeValue
    
    progress = currentTime / duration
    
    eased_progress = easingFunction(progress)
    
    currentValue = beginValue + eased_progress * changeValue
    
    return currentValue


def ease_map(currentVal, startVal, endVal, startValue, endValue, easingFunction):
    
    if currentVal <= startVal:
        return startValue
    elif currentVal >= endVal:
        return endValue
    
    c = endValue - startValue
    d = endVal - startVal
    
    return ease(currentVal, startValue, c, d, easingFunction)

############
# These functions output a value from 0 to 1
############

def ease_in_sine(x):
    return 1 - math.cos((x * math.pi) / 2)

def ease_out_sine(x):
    return math.sin((x * math.pi) / 2)

def ease_in_out_sine(x):
    return -(math.cos(math.pi * x) - 1) / 2

# polynomial easing
# exp: 2 = quad, 3 = cubic, 4 = quart, 5 = quint etc
def ease_in_poly(x, exp=2):
    return pow(2, exp)

def ease_out_poly(x, exp=2):
    return 1 - math.pow(1 - x, exp)

def ease_in_out_poly(x, exp=2):
    return pow(2, exp-1) * math.pow(x, exp) if x < 0.5 else 1 - math.pow(-2 * x + 2, exp) / 2

def ease_in_quad(x):
    return x * x

def ease_out_quad(x):
    return 1 - (1 - x) * (1 - x)

def ease_in_out_quad(x):
    return 2 * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 2) / 2

def ease_in_cubic(x):
    return x * x * x

def ease_out_cubic(x):
    return 1 - math.pow(1 - x, 3)

def ease_in_out_cubic(x):
    return 4 * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 3) / 2

def ease_in_quart(x):
    return x * x * x * x

def ease_out_quart(x):
    return 1 - math.pow(1 - x, 4)

def ease_in_out_quart(x):
    return 8 * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 4) / 2

def ease_in_quint(x):
    return x * x * x * x * x

def ease_out_quint(x):
    return 1 - math.pow(1 - x, 5)

def ease_in_out_quint(x):
    return 16 * x * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 5) / 2

def ease_in_expo(x):
    return 0 if x == 0 else math.pow(2, 10 * x - 10)

def ease_out_expo(x):
    return 1 if x == 1 else 1 - math.pow(2, -10 * x)

def ease_in_out_expo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return math.pow(2, 20 * x - 10) / 2 if x < 0.5 else (2 - math.pow(2, -20 * x + 10)) / 2

def ease_in_circ(x):
    return 1 - math.sqrt(1 - math.pow(x, 2))

def ease_out_circ(x):
    return math.sqrt(1 - math.pow(x - 1, 2))

def ease_in_out_circ(x):
    return (1 - math.sqrt(1 - math.pow(2 * x, 2))) / 2 if x < 0.5 else (math.sqrt(1 - math.pow(-2 * x + 2, 2)) + 1) / 2

def ease_in_back(x):
    c1 = 1.70158
    c3 = c1 + 1
    return c3 * x * x * x - c1 * x * x

def ease_out_back(x):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)

def ease_in_out_back(x):
    c1 = 1.70158
    c2 = c1 * 1.525
    return (math.pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2 if x < 0.5 else (math.pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2

def ease_in_elastic(x):
    c4 = (2 * math.pi) / 3
    return 0 if x == 0 else 1 if x == 1 else -math.pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * c4)

def ease_out_elastic(x):
    c4 = (2 * math.pi) / 3
    return 0 if x == 0 else 1 if x == 1 else math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1

def ease_in_out_elastic(x):
    c5 = (2 * math.pi) / 4.5
    if x == 0:
        return 0
    if x == 1:
        return 1
    return -(math.pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * c5)) / 2 if x < 0.5 else (math.pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * c5)) / 2 + 1

def ease_in_bounce(x):
    return 1 - ease_out_bounce(1 - x)

def ease_out_bounce(x):
    n1 = 7.5625
    d1 = 2.75
    if x < 1 / d1:
        return n1 * x * x
    elif x < 2 / d1:
        return n1 * (x - 1.5 / d1) * x + 0.75
    elif x < 2.5 / d1:
        return n1 * (x - 2.25 / d1) * x + 0.9375
    else:
        return n1 * (x - 2.625 / d1) * x + 0.984375

def ease_in_out_bounce(x):
    return (1 - ease_out_bounce(1 - 2 * x)) / 2 if x < 0.5 else (1 + ease_out_bounce(2 * x - 1)) / 2
