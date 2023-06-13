import cv2

path = "chapter3\human.jpg"
img = cv2.imread(path)

# 画像の表示
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 画像の保存
# cv2.imwrite("chapter3\human_copy.jpg", img)

# # 画像のサイズを変更
# img2 = cv2.resize(img, (300, 300))
# cv2.imshow("img2", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 画像の一部を切り取り
# img3 = img[100:300, 200:400]
# cv2.imshow("img3", img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 画像の回転
# img_rotate = cv2.rotate(img, cv2.ROTATE_180)
# cv2.imshow("img_rotate", img_rotate)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 画像に文字の刻印
# cv2.putText(img, 
#             "Hello", 
#             (100, 100), 
#             cv2.FONT_HERSHEY_TRIPLEX, 
#             1.0, 
#             (0, 255, 0), 
#             thickness=2,
#             lineType=cv2.LINE_AA)

# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 円の描画
# cv2.circle(img, 
#            (200, 200), 
#            100, 
#            (0, 255, 0), 
#            thickness=2,
#            lineType=cv2.LINE_AA)

# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 画像のグレースケール化
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("img_gray", img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 四角形の描画
# cv2.rectangle(img,
#               (0, 0),
#               (400, 400),
#               (0, 255, 0),
#               thickness=2,
#               lineType=cv2.LINE_AA)

# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 画像に直線を描画する
# cv2.line(img,
#          (0, 0),
#          (400, 400),
#          (0, 255, 0),
#          thickness=2,
#          lineType=cv2.LINE_AA)

# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 画像に矢印線を描画する
# cv2.arrowedLine(img,
#                 (0, 0),
#                 (400, 400),
#                 (0, 255, 0),
#                 thickness=2,
#                 line_type=cv2.LINE_AA,
#                 tipLength=0.1)

# 画像にポインターを描画する
# cv2.drawMarker(img,
#                 (200, 200),
#                 (0, 255, 0),
#                 markerType=cv2.MARKER_CROSS,
#                 markerSize=10,
#                 thickness=2,
#                 line_type=cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
