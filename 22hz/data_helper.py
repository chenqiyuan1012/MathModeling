import numpy as np
import pandas as pd
import matplotlib as plt

df=pd.read_excel("1_1.xls",sheet_name="1")
print(df.iloc[1,:])