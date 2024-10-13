import pandas as pd

df = pd.DataFrame( {'values' : [val for val in range(1, 101)]})
"""статистические данные числового списка чисел 1..100"""
description = df['values'].describe()
print(description)

"""чтение из файла"""
df = pd.read_csv("file 2.txt", sep=" ")
print(df)
