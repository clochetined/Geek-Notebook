import numpy as np
import pandas as pd

col1 = np.array([1, 2, 3])
col2 = np.array([4, 5, 6])
col3 = np.array([7, 8, 9])

df = pd.DataFrame({"col1": col1, "col2": col2, "col3": col3})
print(df.head())