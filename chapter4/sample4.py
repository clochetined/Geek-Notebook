import numpy as np
from PIPL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud as get_wordcrowd

def get_wordcrowd_mask(text, imagepath):
    img_color = np.array(Image.open(imagepath))
    wc = get_wordcrowd(
        width=900,
        height=500,
        background_color="white",
        font_path="C:/Windows/Fonts/YuGothR.ttc",
        mask=img_color,
        collections = False,# 単語の重複しないように
    ).generate(text)

    # 図のサイズを6*6指定、1インチあたりのドット数を200に指定
    plt.figure(figsize=(15, 12), dpi=200)
    # 画像を補完
    plt.imshow(wc, interpolation='bilinear')
    # サブプロットの軸をオフに設定
    plt.axis("off")
    # 画像を表示
    plt.show()

get_wordcrowd_mask(text, "chapter4\sample3.png")
 