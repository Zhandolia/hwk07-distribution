import numpy as np

from hwk07_p2_soln import project, rotate

# NOTE: you do NOT need to rewrite the `project` or `rotate` functions 
# as they are imported above

def moveTo(start, end):
    """
    returns the matrix corresponding to moving an obj 
    from position 'start' to position 'end.'
    positions are given in 3D homogeneous coordinates.
    """
    # return np.eye(4)
    return np.array([[
        [1, 0, 0, end[0] - start[0]],
        [0, 1, 0, end[1] - start[1]],
        [0, 0, 1, end[2] - start[2]],
        [0, 0, 0, 1]
    ]])

def ballTransform3(i, loc):
    """
    returns the appropriate transformation matrix for the ball.
    The center of the ball before transformation is given by 'loc'.  
    The appropriate transformation depends on the
    timestep which is given by 'i'.
    """
    # return np.eye(4)
    P = project(100.0)
    finalSet = np.array([20, 0, 0, 1])
    T = moveTo(loc, loc + (i/150) * finalSet)
    return P @ T
