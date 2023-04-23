import json
import xml.etree.ElementTree as ET

with open('addres-book.json', 'r') as f:
    data = json.load(f)

for entry in data:
    if 'email' in entry:
        print(entry['email'])

print('--------------------------')

for entry in data:
    if 'phones' in entry:
        for phone in entry['phones']:
            print(phone['phone'])

print('--------------------------')

tree = ET.parse('addres-book-q.xml')
root = tree.getroot()
phones_list = []

for address in root.iter('address'):
    phones_dict = {}
    name = address.find('name').text
    phones_dict['name'] = name

    for phone in address.findall('phones/phone'):
        number = phone.text
        type = phone.get('type')
        phones_dict[type] = number

    phones_list.append(phones_dict)

print(phones_list)
