import numpy as np


def project(d):
    """
    returns the projection matrix corresponding to having the 
    viewpoint at (0, 0, d)
    and the viewing plane at z = 0 (the xy plane).
    """
    return(np.eye(4))

def houseTransform1(i, loc):
    """
    Returns the appropriate transformation matrix for the house, 
    which in this case is simply the projection matrix at d=100.
    """
    return np.eye(4)

def ballTransform1(i, loc):
    """
    Returns the appropriate transformation matrix for the ball,
    which in this case is simply the projection matrix at d=100.
    """
    return np.eye(4)
