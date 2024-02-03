import pandas as pd
from google.colab import drive 

drive.mount('/content/drive')
sample =  pd.read_csv("/content/drive/MyDrive/sample.csv") 
print(sample.head())