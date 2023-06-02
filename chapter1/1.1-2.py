import pandas as pd
import numpy as num
import random

s = pd.Series([1 , 2, 3, 4])
print(s)

def hello():
    print('hello')
hello()


def add(a,b):
    x = a*b
    return x

answer = add(70 ,30 )
print(answer)

#**kwargs: 複数のキーワード引数を辞書として受け取る
def func_kwargs(**kwargs):
    print(kwargs)

func_kwargs(a = 1 ,b = 2)
print(func_kwargs)

#リストやタプルを展開して指定
#関数呼び出し時にリストやタプルに*をつけて指定すると、要素が展開（アンパック）され順番に位置引数として指定される。要素数と引数の数が一致していないとエラー（TypeError）になる。
def func(a ,b ,c):
#f文字列（フォーマット文字列）の基本的な使い方 : 文字列メソッドformat()では、順番に引数を指定したり名前を決めてキーワード引数で指定したりして置換フィールド{}に値を挿入できる。
    print(f'a = {a} ,b = {b} ,c = {c}')

num_list = [1 ,2 ,3]
func(*num_list)


#str 関数は引数に指定したオブジェクトを文字列にして取得します。
print("Mypage" + str(100))

#range 関数は引数に指定した開始数から終了数までの連続した数値を要素として持つ range 型のオブジェクトを作成します。
s = range(4, 7)
print(list(s))

s = range(2 ,9 , 2)
print(list(s))


#関数とメソッドの違い
#単独で呼び出しできるのが「関数」   Pythonの組み込み関数のprint()、len()などは単独で呼び出せる「関数」
#変数や値に付けて呼び出すのが「メソッド」   リストに要素を追加するappend()や文字列を繋ぐjoin()は変数や値に付けて呼び出す「メソッド」

num_list = ["one" ,"two" ,"three"]
num_list.append("four")
num_list = "+".join(num_list)

print(num_list)

org_list = [3, 1, 4, 5, 2]
org_list.sort(reverse=True)

print(org_list)


#strデータ（文字列）を単独の区切り文字で分割する
#空白文字にはスペースや改行\n, タブ\tが含まれ、連続する空白文字はまとめて処理される。
s_blank = "one    two    three\nfive\tfive"
print(s_blank)
print(s_blank.split("n"))

#input関数
#input関数とは、キーボードから入力した文字や数値を受け取るための関数
#input関数の引数には、ユーザーに表示させたい文字列を与える必要があります
name = input("名前")
print("your name is" + name + ",isn't you")

height = float(input("height[cm]"))
weight = float(input("weght[kg]"))

height /= 100 # [m]
bmi = weight/(height**2)

print(round(bmi ,1))

#enumerate関数を使うと、要素のインデックスと要素を同時に取り出す事が出来ます
meal = ["morning" ,"afternoon" , "dinner"]
for i,j in enumerate(meal):
    print("{}:{}".format(i ,j))

print(random.randint(1 ,100))
print(random.uniform(0 ,1))

#リスト内包表記
list_a = []
for i in range(10):
    list_a.append(i**2)

print(list_a)

list_b = [i**2 for i in range(10)]
print(list_b)
