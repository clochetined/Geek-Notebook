def hello():
    print("hello")

hello()

str_list = ['a','b','c']
num_list = [1,2,3,4,5]

print(num_list[2])

print(str_list[1:])

#要素を指定して削除
str_list.remove('a')
print(str_list)

#要素番号を指定して削除
del str_list[0]
print(str_list)

#要素を追加する
str_list.append('d')
print(str_list)

#タプル
a = (0, 1, 8, 12)
print(a)

print(a[2])
#タプルは要素を変更できない

dict = {'a':20 ,'b':30 ,'c':15 }

#keyからValueを指定
print(dict['a'])

#一覧取得keys,valuesメソッド
print(dict.keys())

#itemメソッドでkey,valueのタプルが並んだリストを取得
print(dict.items())


#setは集合を表すデータ型、順番要素を持たない、重複要素は取り除かれる
s = set([1 ,2 ,3 ,4 ,5 ])

#セットに要素を追加するにはaddメソッド
print(s.add(6))

#setから要素を削除するには
print(s.remove(3))

print(s.clear())


