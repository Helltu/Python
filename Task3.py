import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Импортировать датасет
df = pd.read_csv('test.csv')

# Взять 1000 значений из выбранного датасета
df_subset = df.head(1000)

# Проверить данные на пропуски
missing_values = df_subset.isnull().sum()
print('Пропущенные данные')
print(missing_values)

# Определить сколько в выборке 1, 2, 3 …комнатных квартир
room_counts = df_subset['Rooms'].value_counts()
print('Количество n-комнатных квартир в выборке')
print(room_counts)

fig, axes = plt.subplots(4, 5, figsize=(20, 20))

# Итерация по колонкам и подграфикам
for i, column in enumerate(df_subset.columns):
    # Вычисляем индексы строки и столбца для текущего подграфика
    row_index = i // 5
    col_index = i % 5
    axes[row_index, col_index].set_title(column)
    
    if pd.api.types.is_numeric_dtype(df_subset[column]):
        # Преобразуем значения в числовой тип данных
        values = pd.to_numeric(df_subset[column])
        # Строим ящик с усами для текущего столбца в текущем подграфике
        axes[row_index, col_index].boxplot(values)
        axes[row_index, col_index].set_yscale('log')

plt.show()

fig, axes = plt.subplots(4, 5, figsize=(20, 20))

# Итерация по колонкам и подграфикам
for i, column in enumerate(df_subset.columns):
    # Вычисляем индексы строки и столбца для текущего подграфика
    row_index = i // 5
    col_index = i % 5
    axes[row_index, col_index].set_title(column)
    
    if pd.api.types.is_numeric_dtype(df_subset[column]):
        # Преобразуем значения в числовой тип данных
        values = pd.to_numeric(df_subset[column])
        # Строим гистограмму для текущего столбца в текущем подграфике
        axes[row_index, col_index].hist(values, 10)
        axes[row_index, col_index].set_yscale('log')

plt.show()

# Заполнить пропуски
for column in df_subset.columns:
    df_subset.loc[:, column] = df_subset[column].fillna(0)

df_subset = df_subset[(df_subset['Square'] > 20) & (df_subset['Square'] < 200)]

# Построить сводную таблицу
pivot_table = pd.pivot_table(df_subset, values='Id', index='DistrictId',
                             columns='Rooms', aggfunc='count', fill_value=0)

print(pivot_table)

# Итоговый обработанный массив без выбросов и пропусков
df_subset.to_csv('surname.csv', index=False)
