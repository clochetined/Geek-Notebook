from matplotlib import pyplot as plt
import cv2

import numpy as np

filename = "chapter3\human.jpg"
orig = cv2.imread(filename)
src = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)

blured = cv2.blur(src, (20, 20))
plt.imshow(blured)
plt.show()