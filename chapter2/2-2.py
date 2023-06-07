import pandas as pd

# インデックスが左側、データの値が右側に出力されています。numpyと同様にindexを指定することで要素を抽出できます。
a = pd.Series([1, 2, 3, 4, 5])
print(a)

# インデックスを指定して要素を抽出
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# 算術メソッドを使って、平均や合計を求める
print(int(a.mean()))
print(a.sum())

# DataFrameにすることで多次元データをテーブル形式で表現する
# DataFrameはSeriesを複数束ねたものと考えることができます。
# 例えば、以下のようにSeriesを複数束ねることでDataFrameを作成することができます。
col_1 = pd.Series([1, 2, 3, 4, 5])
col_2 = pd.Series([10, 20, 30, 40, 50])
col_3 = pd.Series([100, 200, 300, 400, 500])

# df = pd.DataFrame([col_1, col_2, col_3])
# print(df)
# print(df[0])
# print(df[1])
# print(df[2])
# print(df.head(1))

# index = [2015, 2016, 2017, 2018, 2019]
# colums = ["menber", "club", "score", "rank"]

# data = [
#     ["Yamada", "Baseball", 15, 1],
#     ["Suzuki", "Soccer", 8, 2],
#     ["Sato", "Tennis", 12, 3],
#     ["Tanaka", "Tennis", 7, 4],
#     ["Ito", "Baseball", 10, 5]
# ]

# df = pd.DataFrame(data, index=index, columns=colums)

# print(df)



data = pd.read_csv("data.csv")
print(data)


