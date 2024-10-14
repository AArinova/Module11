import pandas as pd
import numpy as np

df = pd.DataFrame({'values': [val for val in range(1, 101)]})

"""Статистические данные числового списка чисел 1..100"""
description = df['values'].describe()
print(description)

"""Чтение из csv- файла"""
df = pd.read_csv("file1.txt", sep=",")
print("\nВывод информации целиком:\n", df)

print("\nВывод названий животных:\n", df[['animal']])

"""Фильтрация данных (только тигры)"""
print("\nТигры:\n")
print(df[df['animal'] == 'tiger'])

"""Фильтрация данных (те животные кому нужно воды > 500л)"""
new_df = df[df['water_need'] >= 500]
print("\nКому требуется больше 500л воды:\n", new_df)

"""Массивы чисел (numpy)"""

nlist = np.array([val for val in range(1, 10)])
print("\nМассив чисел от 1 до 1000:\n", nlist)
nlist2 = np.sqrt(nlist)
print("\nМассив все элементы которого являются квадратными корнями предыдущего массива:\n", nlist2)
print("\nРазность этих массивов:\n", nlist - nlist2)
print("\nМатричное произведение этих массивов:\n", nlist.dot(nlist2))

rn_list = np.random.random((3,5))
print("\nМногомерный массив случайных чисел (матрица) размером 3х5:\n", rn_list)
print("\nСумма всех элементов массива:", rn_list.sum())
print("\nМинимальное значение массива:", rn_list.min())
print("\nМаксимальное значение массива:", rn_list.max())

