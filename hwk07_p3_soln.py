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
    dx, dy, dz = end - start
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])

def ballTransform3(i, loc):
    """
    returns the appropriate transformation matrix for the ball.
    The center of the ball before transformation is given by 'loc'.  
    The appropriate transformation depends on the
    timestep which is given by 'i'.
    """
    return np.eye(4)
