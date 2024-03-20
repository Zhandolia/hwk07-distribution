import numpy as np
import matplotlib.pyplot as plt
import sys

# use '.' below for the current working directory
# else replace '.' with the path to the folder where your files are
sys.path.append('.')
from Homework07 import HouseBallAnimation
from hwk07_p2_soln import houseTransform2
from hwk07_p4_soln import project, moveTo, rotate, ballTransform4

obj = HouseBallAnimation(show_axes = True)
anim = obj.animate(ballTransform4, houseTransform2)
plt.show()
# use the following format to create an MPEG video that can be viewed in quicktime
# you may need 'brew install ffmpeg'
# anim.save('hwk07Solution.mp4', fps=20)
# use the following format to create a video that can be viewed in a browser
# anim.save('hwk07Solution-browser.mp4', fps=20, extra_args=['-vcodec', 'libx264'])

