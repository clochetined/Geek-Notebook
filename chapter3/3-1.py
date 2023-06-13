
# ライブラリのインポート
# matplotlibのインポート。今後pltという名前で用いる。
from matplotlib import pyplot as plt

# OpenCVのインポート
import cv2

# 画像ファイルの読み込み
# 同じ階層にあるため、ファイル名のみ記述
filename = "chapter3\証明写真.jpg"

# 画像配列の生成
orig = cv2.imread(filename)

# RGBの順に整形
src = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)

# 配列の形を表示(たて座標 x 横座標 x 3色の値)
print(src.shape)

# 画像の表示
plt.imshow(src)
plt.show()