import pandas as pd

read_csv = pd.read_csv("chapter2\weather.csv")

# print(read_csv.columns)

# read_csv.columnsにある.1と.2を削除する
# read_csv = read_csv[[col for col in read_csv.columns if ".1" not in col and ".2" not in col]]
for col in read_csv.columns:
    if ".1" in col or ".2" in col:
        read_csv = read_csv.drop(col, axis=1)

print(read_csv.head(5))
read_csv[1:]

print(read_csv.iloc[5:11, 2:6])
print(read_csv.loc[5:10, "最高気温(℃)":"最深積雪(cm)"])
