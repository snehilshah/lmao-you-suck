import re

my_list = ['person1', 'car', 'person2', 'tree', 'person3']

person_list = []

for item in my_list:
    if re.search(r'person', item):
        person_list.append(item)


print(person_list)
