import pandas as pd
import numpy as np

df = pd.DataFrame({'values': [val for val in range(1, 101)]})

"""статистические данные числового списка чисел 1..100"""
description = df['values'].describe()
print(description)

"""чтение из csv- файла"""
df = pd.read_csv("file1.txt", sep=",")
print("\nВывод информации целиком:\n", df)

print("\nВывод названий животных:\n", df[['animal']])

"""Фильтрация данных (только тигры)"""
print("\nТигры:\n")
print(df[df['animal'] == 'tiger'])

"""Фильтрация данных (те животные кому нужно воды > 500л)"""
new_df = df[df['water_need'] >= 500]
print("\nКому требуется больше 500л воды:\n", new_df)

"""Массивы чисел"""

nlist = np.array([val for val in range(1, 101)])
print("\nМассив чисел от 1 до 1000:\n", nlist)

rn_list = np.random.random((2,3))
print("\nМассив случайных чисел:\n", rn_list)
print("\nСумма всех элементов массива:\t", rn_list.sum())

