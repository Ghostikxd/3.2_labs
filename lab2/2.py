import pandas as pd
import numpy as np
import datetime

# 1.1
recipes = pd.read_csv("recipes_sample.csv")
reviews = pd.read_csv("reviews_sample.csv", index_col=0)

# 1.2
""" recipes.info()  # общая информация о таблице recipes
print('Количество точек данных (строк) в таблице reviews:\n', len(reviews))
print('Количество столбцов в таблице reviews:\n', len(reviews.columns))
print('Тип данных каждого столбца в таблице reviews:\n', reviews.dtypes) """

# 1.3
""" recipes_missing = recipes.isnull().any()
reviews_missing = reviews.isnull().any()
print("\nСтолбцы таблицы recipes c пропусками:")
print(recipes_missing[recipes_missing].index.tolist())
print("\nСтолбцы таблицы reviews c пропусками:")
print(reviews_missing[reviews_missing].index.tolist())
recipes_missing_rows = recipes.isnull().any(axis=1).mean()
reviews_missing_rows = reviews.isnull().any(axis=1).mean()
print("\nДоля строк таблицы recipes с пропусками: {:.2%}".format(
    recipes_missing_rows))
print("Доля строк таблицы reviews с пропусками: {:.2%}".format(
    reviews_missing_rows)) """

# 1.4
""" num_recipes = recipes.select_dtypes(include=['int64', 'float64']).columns
mean_values_recipes = recipes[num_recipes].mean().round(2)
print('Среднее значение для числовых столбцов в таблице recipes:')
print(mean_values_recipes)
num_reviews = reviews.select_dtypes(include=['int64', 'float64']).columns
mean_values_reviews = reviews[num_reviews].mean().round(2)
print('Среднее значение для числовых столбцов в таблице reviews:')
print(mean_values_reviews) """
# print(reviews.describe().round(2)) общая статистика каждого столбца таблицу reviews

# 1.5
""" recipes = pd.read_csv('recipes_sample.csv')
recipe_names = recipes['name'].sample(
    n=10, random_state=np.random.seed()).reset_index(drop=True)
print(recipe_names) """

# 1.6
""" reviews = reviews.reset_index(drop=True) """

# 1.7
""" usl_recipes = recipes.loc[(recipes['minutes'] <= 20) & (
    recipes['n_ingredients'] <= 5)]
print(usl_recipes) """

# 2.1
""" recipes['submitted'] = pd.to_datetime(recipes['submitted'], format='%Y-%m-%d')
print(recipes['submitted']) """

# 2.2
""" recipes_date = recipes[recipes['submitted'] < '2010-01-01']
print(recipes_date) """

# 3.1
""" recipes_description = recipes['description_length'] = recipes['description'].apply(
    lambda x: len(str(x)))
print(recipes_description) """

# 3.2
""" recipes_uppercase = recipes['name'] = recipes['name'].str.title()
print(recipes_uppercase) """

# 3.3
""" 

def count_words(name):
    words = filter(lambda x: x != '', name.split(' '))
    return len(list(words))


recipec_count_words = recipes['name_word_count'] = recipes['name'].apply(
    count_words)
print(recipec_count_words) """

# 4.1
""" recipe_contributions = recipes['contributor_id'].value_counts()
max_contributor_id = recipe_contributions.idxmax()

print(f"Участник с id {max_contributor_id} добавил максимальное количество рецептов: {recipe_contributions[max_contributor_id]}") """

# 4.2
""" avg_ratings = reviews[reviews['rating'] > 0].groupby('recipe_id')[
    'rating'].mean()
num_no_reviews = reviews['review'].isnull().sum()
print("Средний рейтинг к каждому из рецептов:\n", avg_ratings)
print("Количество рецептов без отзывов:", num_no_reviews) """

# 4.3
""" recipes['submitted'] = pd.to_datetime(recipes['submitted'], format='%Y-%m-%d')
recipes['year_created'] = recipes['submitted'].dt.year
recipe_count_by_year = recipes['year_created'].value_counts()
print(recipe_count_by_year) """

# 5.1
""" merged = pd.merge(recipes, reviews, how='inner',
                  left_on='id', right_on='recipe_id')
recipes_with_ratings = merged[['id', 'name', 'user_id', 'rating']]
recipes_with_ratings = recipes_with_ratings[recipes_with_ratings['rating'] > 0]
print(recipes_with_ratings)
# print(merged[merged['id'] == 453285])  # использовать для проверки """

# 5.2
""" recipes_reviews = recipes.merge(
    reviews, left_on='id', right_on='recipe_id', how='left')
recipe_review_count = recipes_reviews.groupby(
    ['id', 'name'], as_index=False)['rating'].count()
recipe_review_count = recipe_review_count.rename(
    columns={'rating': 'review_count'})
print(recipe_review_count[['id', 'name', 'review_count']]) """

# 5.3
""" merged_data = pd.merge(recipes, reviews, left_on='id', right_on='recipe_id')
grouped_data = merged_data.groupby('year_created')[
    'rating'].mean().reset_index()
min_rating_year = grouped_data.sort_values('rating').iloc[0]['year_created']
print(min_rating_year) # для корректной работы нужен пункт 4.3"""

# 6.1
""" recipes_sorted = recipes.sort_values(by='name_word_count', ascending=False)
print(recipes_sorted)
recipes_description.to_csv('recipes_description.csv', index=False)
recipes_uppercase.to_csv('recipes_uppercase.csv', index=False)
recipec_count_words.to_csv('recipec_count_words.csv', index=False) # для корректной работы нужны пунтку 3.1, 3.2, 3.3"""

# 6.2
""" recipes_with_ratings.to_excel(
    'recipes_with_ratings.xlsx', sheet_name='Рецепты с оценками', index=False)
recipe_review_count.to_excel('recipe_review_count.xlsx',
                             sheet_name='Количество отзывов по рецептам', index=False) # для корректной работы нужны пунтку 5.1, 5.2"""
