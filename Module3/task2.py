def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [10, 'test', False]
values_dict = {'a': 20, 'b': 'aboba', 'c': [4, 5, 6]}

print_params(*values_list)
print_params(**values_dict)