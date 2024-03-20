import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('.')  # or wherever you have placed Homework07.py
from Homework07 import HouseBallAnimation

def houseTransform0(i, loc):
    """
    Simply returns the identity matrix, to show setup before projection
    """
    P = np.eye(4)
    return P

def ballTransform0(i, loc):
    """
    Simply returns the identity matrix, to show setup before projection
    """
    P = np.eye(4)
    return P 

obj = HouseBallAnimation(show_axes = True)
anim = obj.animate(ballTransform0, houseTransform0)
plt.show()
