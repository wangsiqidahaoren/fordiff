import numpy as np
def reverse(x, axes):
    if isinstance(axes, list):
        axes = tuple(axes)
    return np.flip(x, axes)