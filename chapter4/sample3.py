from janome.tokenizer import Tokenizer

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

print(gakutika_list)
