import numpy as np

from hwk07_p3_soln import moveTo, project, rotate

# NOTE: you do NOT need to rewrite the `project`, `rotate`, or `moveTo` functions 
# as they are imported above

def ballTransform4(i, loc):
    """
    returns the appropriate transformation matrix for the ball.
    The center of the ball before transformation is given by 'loc'.  
    The appropriate transformation depends on the
    timestep which is given by 'i'.
    """
    # return np.eye(4)
    P = project(100.0)
    M = moveTo(loc, np.zeros[4])
    R = rotate(0, 0, -2.0 * np.pi * (i/150))
    finalSet = np.array([20, 0, 0, 1])
    T = moveTo(np.zeros(4), loc + (i/150) * finalSet)
    return P @ T @ R @ M
    