import cv2
import numpy as np

path = 'chapter3\liner.png'
img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 画像のビットを反転させる
reverse = cv2.bitwise_not(gray)
# 直線の検出
lines = cv2.HoughLinesP(reverse, 
                        1, 
                        np.pi/180, 
                        100,
                        minLineLength=100, 
                        maxLineGap=10)
# print(lines)

for line in lines:
    print(line)
    x1, y1, x2, y2 = line[0]

    line_img = cv2.line(img, 
             (x1, y1), 
             (x2, y2), 
             (0, 255, 0), 
             3)

cv2.imwrite('chapter3\liner_result.png', line_img)