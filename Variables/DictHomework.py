my_dict = {'name': 'Andrei', 'surname': 'Ivanov', 'age': 35}
print("Dictionary: ", my_dict)
print(my_dict['name'])
my_dict['occupation'] = 'Python Developer'
my_dict['hobby'] = 'sewing'
del my_dict['age']
print("Modified Dictionary: ", my_dict)

my_set = {1, 'hello', False}
print("Set: ", my_set)
my_set.add(77)
my_set.add('string')
my_set.remove(1)
print("Modified Set: ", my_set)
