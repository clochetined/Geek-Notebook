import pandas as pd
from google.colab import drive 

drive.mount('/content/drive')
sample =  pd.read_csv("/content/drive/MyDrive/sample.csv") 
sample
a = pd.Series([1, 2, 3, 4])
print(a)