import cv2 #OpenCV
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("path/to/google/module")
from google.colab import drive #googledriveから画像をとってくるのに必要
drive.mount('/content/drive')

# 画像の読み込み
img = cv2.imread('/content/drive/My Drive/Colab Notebooks/Python3/3-4/lena.jpg')

# 画像の表示
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()