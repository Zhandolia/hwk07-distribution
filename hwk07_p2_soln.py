import numpy as np
from hwk07_p1_soln import project

# NOTE: you do NOT need to rewrite the `project` function 
# as it is imported above

def rotate(x, y, z):
    """
    returns the matrix corresponding to first rotating a value 'x' 
    around the x-axis, 
    then rotating 'y' around the y-axis, 
    and then 'z' around the z-axis.   
    All angles are in radians. 
    The center of rotation is at point given by 'loc' 
    (3D homogeneous coord).
    These matrices obey the right-hand rule: 
    a positive rotation is counter-clockwise
    when looking along the axis of rotation 
    from the positive direction toward the origin.  
    """
    return np.eye(4)

def houseTransform2(i, loc):
    """
    returns the appropriate transformation matrix for the house.  
    The center of the house before transformation is given by 'loc'.  
    The appropriate transformation depends on the
    timestep which is given by 'i'.
    """
    return np.eye(4)
