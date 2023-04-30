import xml.etree.ElementTree as ET
import json
import pandas as pd
import pickle

# 1.1
""" with open('contributors_sample.json') as f:
    data = json.load(f)

print(data[:3]) """

# 1.2
""" with open('contributors_sample.json') as f:
    data = json.load(f)

email_domains = set()

for person in data:
    email = person['mail']
    domain = email.split('@')[1]
    email_domains.add(domain)

for domain in email_domains:
    print(domain) """

# 1.3
""" def find_user_by_username(username):
    with open('contributors_sample.json') as f:
        data = json.load(f)

        for user in data:
            if user['username'] == username:
                return user

        raise ValueError('User not found')


username = find_user_by_username('uhebert')
print(username) """

# 1.4
""" with open('contributors_sample.json') as f:
    data = json.load(f)

males = 0
females = 0

for person in data:
    if person['sex'] == 'M':
        males += 1
    elif person['sex'] == 'F':
        females += 1

print('Количество мужчин:', males)
print('Количество женщин:', females) """

# 1.5
""" contributors = pd.DataFrame(columns=['id', 'username', 'sex']) """

# 1.6
""" recipes = pd.read_csv('recipes_sample.csv')
merged_data = pd.merge(recipes, contributors, on='id', how='left')
missing_contributors = merged_data['name'].isnull().sum()
print(f'Информация отсутствует для {missing_contributors} человек')
# для корректной работы нужен пунтк 1.6 """

# 2.1
""" with open('contributors_sample.json') as f:
    data = json.load(f)

jobs = {}

for person in data:
    for job in person['jobs']:
        if job not in jobs:
            jobs[job] = [person['username']]
        else:
            jobs[job].append(person['username'])

print(jobs) """

# 2.2
""" with open('job_people.pickle', 'wb') as f:
    pickle.dump(jobs, f)

with open('job_people.json', 'w') as f:
    json.dump(jobs, f, indent=4) """

# 2.3
""" with open('job_people.pickle', 'rb') as f:
    job_people = pickle.load(f)

print(job_people) """

# 3.1
""" tree = ET.parse('steps_sample.xml')
root = tree.getroot()

steps = {}

for recipe in root.findall('recipe'):
    recipe_id = recipe.find('id').text
    steps_list = []
    for step in recipe.find('steps').iter('step'):
        steps_list.append(step.text)
    steps[recipe_id] = steps_list

with open('steps_sample.json', 'w') as f:
    json.dump(steps, f) """

# 3.2
""" tree = ET.parse('steps_sample.xml')
root = tree.getroot()
steps_dict = {}
for recipe in root.iter('recipe'):
    recipe_id = recipe.find('id').text
    steps = recipe.findall('steps/step')
    num_steps = len(steps)
    if num_steps in steps_dict:
        steps_dict[num_steps].append(recipe_id)
    else:
        steps_dict[num_steps] = [recipe_id]

print(steps_dict) """

# 3.3
""" tree = ET.parse('steps_sample.xml')
root = tree.getroot()
recipes_with_time = []

for recipe in root.findall('recipe'):
    for step in recipe.findall('steps/step'):
        if 'has_minutes' in step.attrib or 'has_hours' in step.attrib:
            recipes_with_time.append(recipe.find('id').text)
            break

print(recipes_with_time) """

# 3.4
""" recipes = pd.read_csv('recipes_sample.csv')
missing_steps = recipes['n_steps'].isnull()

if missing_steps.any():
    tree = ET.parse('steps_sample.xml')
    root = tree.getroot()

    steps_dict = {}
    for recipe in root.findall('recipe'):
        id = int(recipe.find('id').text)
        steps_count = float(len(recipe.findall('steps/step')))
        steps_dict[id] = steps_count

    recipes.loc[missing_steps, 'n_steps'] = recipes.loc[missing_steps,
                                                        'id'].map(steps_dict)
print(recipes.head()) """

# 3.5
""" recipes['n_steps'] = recipes['n_steps'].astype(int)
recipes.to_csv('recipes_sample_with_filled_nsteps.csv', index=False)
# для корректной работы нужен пункт 3.6 """
