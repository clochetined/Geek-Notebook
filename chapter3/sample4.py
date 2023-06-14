from matplotlib import pyplot as plt
import cv2
import numpy as np

filename = "chapter3\human.jpg"
orig = cv2.imread(filename)

src = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)

# 範囲(left, top, right, bottom) 数値は任意
roi = (60, 60, 200, 200)

pixel = np.array(src)

# 範囲内の画素値を反転
for y in range(roi[1], roi[3]):
    for x in range(roi[0], roi[2]):
        pixel[y][x] = 255 - pixel[y][x]

plt.imshow(pixel)
plt.show()
