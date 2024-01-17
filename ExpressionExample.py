import numpy as np
def reverse(x, axes):
    if isinstance(axes, int):
        axes = [axes]
    for a in axes:
        x = np.flip(x, a)
    return x