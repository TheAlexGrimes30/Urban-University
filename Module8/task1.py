def add_everything_up(first_var, second_var):
    try:
        return first_var + second_var
    except TypeError:
        return str(first_var) + str(second_var)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
