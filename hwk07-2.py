import sys

import matplotlib.pyplot as plt
import numpy as np

# use '.' below for the current working directory
# else replace '.' with the path to the folder where your files are
sys.path.append('.')
from Homework07 import HouseBallAnimation
from hwk07_p1_soln import ballTransform1
from hwk07_p2_soln import houseTransform2, project, rotate

obj = HouseBallAnimation(show_axes = True)
anim = obj.animate(ballTransform1, houseTransform2)
plt.show()
# anim.save('hwk07-2-Solution.mp4', fps=20)
