def test_function():
    def inner_function():
        print("Функция inner_function")

    inner_function()

test_function()

# inner_function невозможно вызвать вне функции test_function