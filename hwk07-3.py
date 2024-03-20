import numpy as np
import matplotlib.pyplot as plt
import sys

# use '.' below for the current working directory
# else replace '.' with the path to the folder where your files are
sys.path.append('.')
from Homework07 import HouseBallAnimation
from hwk07_p2_soln import houseTransform2
from hwk07_p3_soln import project, moveTo, rotate, ballTransform3

obj = HouseBallAnimation(show_axes = True)
anim = obj.animate(ballTransform3, houseTransform2)
plt.show()
# anim.save('hwk07-3-Solution.mp4', fps=20)
