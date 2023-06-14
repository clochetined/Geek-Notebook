from matplotlib import pyplot as plt
import cv2
import numpy as np

filename = "chapter3\human.jpg"
orig = cv2.imread(filename)

src = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)

pixel = np.array(src)
pixel = 255 - pixel

plt.imshow(pixel)
plt.show()
