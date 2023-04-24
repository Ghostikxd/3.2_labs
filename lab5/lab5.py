import csv
import json
import pandas as pd
import numpy as np
import h5py
import os

# 1.1
""" with open('tags_sample.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    tags_dict = {}
    for row in reader:
        id, tag = int(row[0]), row[1]
        if id not in tags_dict:
            tags_dict[id] = []
        tags_dict[id].append(tag)

with open('tags_sample.json', 'w') as f:
    json.dump(tags_dict, f) """

# 1.2
""" recipes_df = pd.read_csv('recipes_sample_with_filled_nsteps.csv')

with open('tags_sample.json', 'r') as f:
    tags_dict = json.load(f)

# Создаем столбец 'n_tags' с количеством тэгов у каждого рецепта
recipes_df['n_tags'] = recipes_df['id'].apply(
    lambda x: len(tags_dict.get(str(x), [])))

# Создаем столбец 'tags' с тэгами в виде строки
recipes_df['tags'] = recipes_df['id'].apply(
    lambda x: '; '.join(tags_dict.get(str(x), [])))
recipes_df['tags'] = recipes_df['tags'].astype('string')

print(recipes_df[['id', 'n_tags', 'tags']])
recipes_df.to_csv('recipes_sample_with_tags.csv', index=False) """

# 1.3
""" ingredients_dict = {}

with open('ingredients_sample.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        recipe_id = int(row['recipe_id'])
        ingredient = row['ingredient']
        if recipe_id not in ingredients_dict:
            ingredients_dict[recipe_id] = []
        ingredients_dict[recipe_id].append(ingredient)

print(ingredients_dict) """

# 1.4
""" ingredients_dict = {}

with open('ingredients_sample.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        id_recipe = row['recipe_id']
        ingredient = row['ingredient']
        if id_recipe in ingredients_dict:
            ingredients_dict[id_recipe].append(ingredient)
        else:
            ingredients_dict[id_recipe] = [ingredient]

recipes_df = pd.read_csv('recipes_sample_with_tags.csv')

recipes_df['n_ingredients'] = recipes_df.apply(
    lambda row: len(ingredients_dict.get(str(row['id']), [])), axis=1)

recipes_df['ingredients'] = recipes_df.apply(
    lambda row: '*'.join(ingredients_dict.get(str(row['id']), [])), axis=1)

print(recipes_df[['id', 'n_tags', 'tags', 'n_ingredients', 'ingredients']]) """


# 1.5
""" if recipes_df['n_ingredients'].isnull().sum() == 0:
    recipes_df['n_ingredients'] = recipes_df['n_ingredients'].astype(int)
    recipes_df.to_csv('recipes_sample_with_tags_ingredients.csv', index=False)
else:
    # для корректной работы нужен был пункт 1.4
    print('В столбце n_ingredients есть пропущенные значения.') """

# 2.1
""" recipes_df = pd.read_csv('recipes_sample_with_tags_ingredients.csv')
recipes_df['year'] = pd.to_datetime(recipes_df['submitted']).dt.year
before_2000 = recipes_df.loc[recipes_df['year']
                             < 2000, ['n_tags', 'n_ingredients']]
after_2000 = recipes_df.loc[recipes_df['year']
                            >= 2000, ['n_tags', 'n_ingredients']]

before_2000_arr = before_2000.to_numpy()
after_2000_arr = after_2000.to_numpy()
print(before_2000_arr)
print(after_2000_arr) """

# 2.2
""" np.savez('recipes_arrays.npz', before_2000=before_2000, after_2000=after_2000)
# для корректной работы нужен был пункт 2.1 """

# 2.3
""" data = np.load('recipes_arrays.npz')

print(data.files)

recipes_2000 = data['before_2000']
recipes_rest = data['after_2000']

print(recipes_2000.shape)
print(recipes_rest.shape)

print(recipes_2000[:5])
print(recipes_rest[:5]) """

# 3.1
""" with h5py.File('nutrition_sample.h5', 'r') as f:
    for i, dataset_name in enumerate(f):
        dataset = f[dataset_name]
        dataset_size = dataset.shape
        metadata = dict(dataset.attrs)
        metadata_str = ', '.join([f"{k} ({v})" for k, v in metadata.items()])
        print(
            f"Dataset name={dataset_name}, dataset size={dataset_size}, metadata={{ {metadata_str} }}")
# некоторые датасеты не содержат атрибут "info" """

# 3.2
""" file = h5py.File("nutrition_sample.h5", 'r')
outfile = h5py.File("nutrition_grouped.h5", 'w')

for dataset_name in file:
    dataset = file[dataset_name]
    over_100 = outfile.create_group(dataset_name + "_over_100PDV")
    less_100 = outfile.create_group(dataset_name + "_less_100PDV")

    for key in dataset.attrs.keys():
        over_100.attrs[key] = dataset.attrs[key]
        less_100.attrs[key] = dataset.attrs[key]

    over_100_data = []
    less_100_data = []

    for row in dataset:
        if row[1] > 100:
            over_100_data.append(row)

        else:
            less_100_data.append(row)

    over_100.create_dataset("data", data=over_100_data)
    less_100.create_dataset("data", data=less_100_data)

file.close()
outfile.close()
 """
# 3.3
""" with h5py.File('nutrition_grouped.h5', 'r') as f:
    for group_name, group in f.items():
        print(f'Group: {group_name}')
        for dataset_name, dataset in group.items():
            print(
                f'\tDataset: {dataset_name}, Shape: {dataset.shape}, Metadata: {dict(dataset.attrs.items())}') """

# 3.4
""" with h5py.File("nutrition_sample.h5", 'r') as file:

    with h5py.File("nutrition_grouped_compressed.h5", 'w') as outfile:

        for dataset_name in file:
            dataset = file[dataset_name]
            over_100 = outfile.create_group(dataset_name + "_over_100PDV")
            less_100 = outfile.create_group(dataset_name + "_less_100PDV")

            for key in dataset.attrs.keys():
                over_100.attrs[key] = dataset.attrs[key]
                less_100.attrs[key] = dataset.attrs[key]

            over_100_data = []
            less_100_data = []

            for row in dataset:
                if row[1] > 100:
                    over_100_data.append(row)
                else:
                    less_100_data.append(row)

            over_100.create_dataset(
                "data", data=over_100_data, compression="gzip")
            less_100.create_dataset(
                "data", data=less_100_data, compression="gzip")


print("Размер файла nutrition_grouped.h5:",
      os.path.getsize("nutrition_grouped.h5"), "байт")
print("Размер файла nutrition_grouped_compressed.h5:",
      os.path.getsize("nutrition_grouped_compressed.h5"), "байт")
print("Разница между размерами этих файлов: ", os.path.getsize("nutrition_grouped.h5")
      - os.path.getsize("nutrition_grouped_compressed.h5"), "байт")
 """
