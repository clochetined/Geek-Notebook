# matplotlib inline
import cv2 #OpenCV
import matplotlib.pyplot as plt
import numpy as np

from google.colab import drive #googledriveから画像をとってくるのに必要
drive.mount('/content/drive')

# 画像を読み込む
fg_img = cv2.imread("/content/drive/My Drive/自分の保存した画像の名前(拡張子付き)")
rgb_fg_img = cv2.cvtColor(fg_img, cv2.COLOR_BGR2RGB)
#画像の表示
plt.imshow(rgb_fg_img)
plt.show()

# 画像をモノクロに変更。
# OpenCVで読み込んだ画像はBGRの順になっている。matplotlibで読み込むためには、RGBの順に並べ替える必要がある。
rgb_fg_img = cv2.cvtColor(fg_img, cv2.COLOR_BGR2RGB)
# 画像をカラーからモノクロに変換する（グレースケール化）。PCの計算量削減・作業メモリ削減のため。
gray = cv2.cvtColor(fg_img, cv2.COLOR_BGR2GRAY)

# 白に置き換える閾値を決めている。159以上の場合、白に変わる。
_, thresh = cv2.threshold(gray, 159, 255, cv2.THRESH_BINARY)

# モノクロ画像を表示
plt.imshow(thresh)
plt.gray()
plt.show()

# マスク画像を生成。
# 画像の輪郭を抽出する。
# cv2.findContours(入力画像, 抽出モード, 近似手法)
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# マスク画像を黒に設定する。
mask = np.zeros_like(thresh)

# 画像の輪郭の内側を白で描画する。
cont_img=cv2.drawContours(mask,contours, -1,(255,255,255),thickness=4)

# 正確なマスク画像作成のため、同じ処理を複数回実施
for i in range(3):
  contours,hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cont_img=cv2.drawContours(mask,contours, -1,(255,255,255),thickness=5)

cv2.fillPoly(mask, contours, color=(255,255,255))

# マスク画像を表示
plt.imshow(mask, cmap='gray')
plt.show()

# 元の画像と配列の形を揃える
mask_stacked = np.dstack([mask]*3)
# マスク画像の白黒の反転
mask_inv = cv2.bitwise_not(mask_stacked) 

# マスク画像とfront画像を合成する
dst = cv2.bitwise_and(rgb_fg_img, mask_stacked)

plt.imshow(dst)
plt.show()