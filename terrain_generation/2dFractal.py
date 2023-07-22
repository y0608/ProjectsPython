# https://nick-aschenbach.github.io/blog/2014/07/06/2d-fractal-terrain/

from matplotlib.pyplot import *
import random


# plt.plot(x1, y1, x2, y2, marker = 'o')
# plt.plot(x1, y1, 'g^', x2, y2, 'g-')
# plot([1, 10, 15], [1, 2, 3], 'go-', label='line 1', linewidth=2)

def generate(y, i):
    if (i >= 2): # end recursion
        plot(y)
        return

    # Find the midpoint for the line segment
    # Assign the midpoint to the average of the endpoints (L + R) / 2
    displacement_value = (y[0] + y[1])/2
    # Generate a random number between -1 to 1 and multiply by the displacement value. 
    randnum = random.uniform(-1, 1)
    print(randnum)
    final = displacement_value + displacement_value * randnum
    # Add this to the midpoint value.
    midpoint = len(y)//2
    y = y[0:midpoint] + [final] + y[midpoint:]  

    generate(y, i+1)


generate([10, 10], 0)
show()