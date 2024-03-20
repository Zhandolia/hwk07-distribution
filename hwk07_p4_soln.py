import numpy as np
from hwk07_p3_soln import project, rotate, moveTo

# NOTE: you do NOT need to rewrite the `project`, `rotate`, or `moveTo` functions 
# as they are imported above

def ballTransform4(i, loc):
    """
    returns the appropriate transformation matrix for the ball.
    The center of the ball before transformation is given by 'loc'.  
    The appropriate transformation depends on the
    timestep which is given by 'i'.
    """
    return np.eye(4)
