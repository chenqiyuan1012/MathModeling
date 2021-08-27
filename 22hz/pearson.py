import pandas as pd
data1 = pd.read_excel("pearson.xls", sheet_name="2")
data2 = pd.read_excel("pearson.xls", sheet_name="3")
print(data1.corr(method='pearson'))
print(data2.corr(method='kendall'))
