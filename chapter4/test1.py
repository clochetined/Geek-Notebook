from janome.tokenizer import Tokenizer
import markovify

# t = Tokenizer()

# for token in t.tokenize('すもももももももものうち'):
#     print(token)

with open("chapter4\origin.txt", encoding="utf-8") as file:
    text = file.read()

# table = {
#     '\n': '', #改行を削除
#     '\r': '', #改行を削除
#     '(': '（', #全角に変更
#     ')': '）', #全角に変更
#     '[': '［', #全角に変更
#     ']': '］', #全角に変更
#     '"': '”', #全角に変更
#     "'": "’" #全角に変更
# }

# text = text.translate(str.maketrans(table))
t = Tokenizer(wakati=True)
text_splitted = list(t.tokenize(text))

text_wakati = ""
for i in range(len(text_splitted)):
    text_wakati += text[i]
    if text_splitted[i] != '。' and text_splitted[i] != '！' and text_splitted[i] != '？':
        text_wakati += ' '
    if text_splitted[i] == '。' or text_splitted[i] == '！' or text_splitted[i] == '？':
        text_wakati += '\t'
# print(text_wakati)

# マルコフ連鎖で文を作る
text_model = markovify.NewlineText(text_wakati)

for _ in range(10):
    print(text_model.make_short_sentence(100).replace(' ', ''))