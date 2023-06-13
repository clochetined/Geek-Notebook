import cv2 
import numpy as np

path = "chapter3\sample.png"
img = cv2.imread(path)

# # 画像のグレースケール化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 円を検出する
circles = cv2.HoughCircles(img_gray,
                            cv2.HOUGH_GRADIENT,
                            dp=1,
                            minDist=20,
                            param1=50,
                            param2=30,
                            minRadius=0,
                            maxRadius=0)

circles = np.uint16(np.around(circles))

for circle in circles[0,:]:
    # 円周を描画する
    cv2.circle(img,
                (circle[0], circle[1]),
                circle[2],
                (0, 255, 0),
                thickness=2,
                lineType=cv2.LINE_AA)
    # 中心点を描画する
    cv2.circle(img,
                (circle[0], circle[1]),
                2,
                (0, 0, 255),
                thickness=2,
                lineType=cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

