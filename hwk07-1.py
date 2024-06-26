import sys

import matplotlib.pyplot as plt
import numpy as np

# use '.' below for the current working directory
# else replace '.' with the path to the folder where your files are
sys.path.append('.')
from Homework07 import HouseBallAnimation
from hwk07_p1_soln import ballTransform1, houseTransform1, project

obj = HouseBallAnimation(show_axes = True)
anim = obj.animate(ballTransform1, houseTransform1)
plt.show()
# anim.save('hwk07-1-Solution.mp4', fps=20)
