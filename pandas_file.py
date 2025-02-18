import pandas as pd
import numpy as np

# Создание DateFrame в ручную
df = pd.DataFrame([[1, 'Bob', 'Builder'],
                   [2, 'Sally', 'Baker'],
                   [3, 'Scott', 'Candle Stick Maker']],
                  columns=['id', 'name', 'occupation'])
print(df)


# Импорт данных
anime = pd.read_csv('anime.csv')
rating = pd.read_csv('rating.csv')
anime_modified = anime.set_index('name')
print(anime)

# Копирование DateFrame
anime_copy = anime.copy(deep=True)


# Экспорт данных
# Создание csv файла с выбронной колонкой #df.to_excel
anime.name[:10].to_csv('saved_ratings.csv', index=False)


#Просмотр и исследование данных
# Вывод первых трех строк DateFrame
print(anime.head(3))

# Вывод последней строки DateFrame
print(rating.tail(1))

# Подсчет количество стрек в Date Frame
print(len(rating))

# Подсчет уникальных строк в df
print(len(rating['user_id'].unique()))

# Получение информации о df
print(anime.info())

# Вывод статистических данных о df
print(anime.describe())

# Подсчёт количества значений
print(anime.type.value_counts())

# Извлечение информации из датафреймов
# Создание списка или объекта Series на основе значений столбца
print(anime['genre'].tolist())
print(anime['genre'])

# Получение списка значений из индекса
print(anime_modified.index.tolist())

# Получение списка значений столбцов
print(anime.columns.tolist())


# Добавление данных в датафрейм и удаление их из него
# Присоединение к датафрейму нового столбца с заданным значением
anime['train_set'] = True
print(anime.info())

# Создание нового датафрейма из подмножества столбцов
print(anime[['name', 'episodes']])

# Удаление заданных столбцов
anime_drop = anime.drop(['anime_id', 'genre', 'members'], axis=1).head()
print(anime_drop)

# Добавление в датафрейм строки с суммой значений из других строк
df1 = pd.DataFrame([[1,'Bob', 8000],
                  [2,'Sally', 9000],
                  [3,'Scott', 20]], columns=['id','name', 'power level'])
df2 = df1.append(df1.sum(axis=0), ignore_index=True) #sum(axis=1)
print(df2)


# Комбинирование датафреймов
# Конкатенация двух датафреймов
df1 = anime[0:2]
print(df1)
df2 = anime[2:4]
print(df2)
print(pd.concat([df1, df2], ignore_index=True))

# Слияние датафреймов
print(rating.merge(anime, left_on='anime_id', right_on='anime_id', suffixes=('_left', '_right')))


#  Фильтрация
#▍Получение строк с нужными индексными значениями
print(anime_modified.loc[['Haikyuu!! Second Season','Gintama']])

# Получение строк по числовым индексам
print(anime_modified.iloc[0:3])

# Получение строк по заданным значениям столбцов
print(anime[anime['type'].isin(['TV'])])  #anime[anime[‘type’] == 'TV']

# Получение среза датафрейма
print(anime[1:3])

# Фильтрация по значению
print(anime[anime['rating'] > 9.4])


#  Сортировка
print(anime.sort_values('rating', ascending=False))


#  Агрегирование
# ▍Функция df.groupby и подсчёт количества записей
print(anime.groupby('type').count())

# Функция df.groupby и агрегирование столбцов различными способам
anime.groupby(["type"]).agg({"rating": "sum", "episodes": "count", "name": "last"}).reset_index().to_csv('saved.csv', index=False)

# Создание сводной таблицы
tmp_df = rating.copy()
tmp_df.sort_values('user_id', ascending=True, inplace=True)
tmp_df = tmp_df[tmp_df.user_id < 10]
tmp_df = tmp_df[tmp_df.anime_id < 30]
tmp_df = tmp_df[tmp_df.rating != -1]
print(pd.pivot_table(tmp_df, values='rating', index=['user_id'], columns=['anime_id'], aggfunc=np.sum, fill_value=0))


# Очистка данных
# ▍Запись в ячейки, содержащие значение NaN, какого-то другого значения
pivot = pd.pivot_table(tmp_df, values='rating', index=['user_id'], columns=['anime_id'], aggfunc=np.sum)
print(pivot)
print(pivot.fillna(0))


# Другие полезные возможности
# Отбор случайных образцов из набора данных
print(anime.sample(frac=0.25))

# Перебор строк датафрейма
for idx,row in anime[:2].iterrows():
    print(idx, row)
