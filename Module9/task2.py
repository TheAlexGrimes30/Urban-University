# Фабрика функций
def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y

        return add
    elif operation == "divide":
        def divide(x, y):
            try:
                return x / y
            except ZeroDivisionError as e:
                print(f"Error: {e}")

        return divide


print("Фабрика функций")
my_func_add = create_operation("add")
print(my_func_add(4, 2))

my_func_divide = create_operation("add")
print(my_func_divide(4, 2))

# Лямбда-функции

print()
print("Лямбда")
square_lambda = lambda x: x ** 2
print(square_lambda(2))


def square_func(x):
    return x ** 2


print(square_func(4))

print()
print("Создание вызываемых объектов")


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rectangle = Rect(2, 4)
print("Стороны:", rectangle.a, ",", rectangle.b)
print("Площадь:", rectangle())
