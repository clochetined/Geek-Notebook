from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd

iris = load_iris()
# iris.data・・・行列データ（分類するための情報）=説明変数
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# iris.target・・・分類先のデータ（分類結果）=目的変数

# irisデータセットを読み込む
iris = sns.load_dataset("iris")

# データの情報を取得
print(iris.info())


# # csvファイルを書き出す
# df.to_csv("data.csv")

