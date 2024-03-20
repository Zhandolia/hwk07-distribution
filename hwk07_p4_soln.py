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
    translation = moveTo(np.array([0, 0, 0]), np.array([i * (20/150.0), 0, 0]))  # Move 20 units over 150 frames
    rotation = rotate(0, 0, (i / 150.0) * 2 * np.pi)  # One full rotation over 150 frames
    return translation @ rotation
