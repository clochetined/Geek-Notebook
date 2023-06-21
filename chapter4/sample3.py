from janome.tokenizer import Tokenizer
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


text_data = open("chapter4\gakutika.txt", "rb").read()
text = text_data.decode('utf-8')

t = Tokenizer()
seps = t.tokenize(text)

gakutika_list = []
tags = ['名詞'#, '動詞', '形容詞', '副詞', '形容動詞', '連体詞', '感動詞', '接続詞', '接頭詞', '助詞', '助動詞', '記号', 'フィラー', 'その他', '未知語']
        ]
def new_func(word, ps):
    print(word, ps)

for _ in seps:
    if _.base_form == '*':
        word = _.surface
    else:
        word = _.base_form
    
    ps = _.part_of_speech
    # new_func(word, ps)
    word_class = ps.split(',')[0]
    # print(word, word_class)
    if word_class in tags:
        gakutika_list.append(word)

# print(gakutika_list)

text = '/'.join(gakutika_list)
# print(text)
fpath = "C:/Windows/Fonts/YuGothR.ttc"
wordcloud = WordCloud(background_color="white", font_path=fpath, width=900, height=500).generate(text)

wordcloud.to_file("chapter4\sample3.png")



def get_wordcrowd_mask(text, imgpath ):
    # 画像を取得して、numpy形式に変換
    img_color = np.array(Image.open(imgpath))
    # wordcloudでの画像形式を設定
    wc = WordCloud(width=800,
                   height=600,
                   font_path=fpath,
                   mask=img_color,
                   collocations=False, # 単語の重複しないように
                  ).generate( text )

    # 図のサイズを6*6指定、1インチあたりのドット数を200に指定
    plt.figure(figsize=(6,6), dpi=200)
    # 画像を補完
    plt.imshow(wc, interpolation="bilinear")
    # サブプロットの軸をオフに設定
    plt.axis("off")
    plt.show()

def get_wordcrowd_color_mask( text, imgpath ):
    img_color = np.array(Image.open( imgpath ))
    wc = WordCloud(width=800,
                   height=600,
                   font_path=fpath,
                   mask=img_color,
                   collocations=False, # 単語の重複しないように
                  ).generate( text )

    image_colors = ImageColorGenerator(img_color) #色情報を追加

    # show
    plt.figure(figsize=(6,6), dpi=200)
    plt.imshow(wc.recolor(color_func=image_colors), # マスク画像の色を使用
               interpolation="bilinear")
    plt.axis("off")
    plt.show()

# get_wordcrowd_mask(text, "chapter4\love.png")
get_wordcrowd_color_mask(text, 'chapter4\love.png')