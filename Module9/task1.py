numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def square(x):
    return x ** 2


def is_odd(x):
    return x % 2 != 0


squared_numbers = map(square, numbers)

odd_squares = filter(is_odd, squared_numbers)

print(list(odd_squares))
