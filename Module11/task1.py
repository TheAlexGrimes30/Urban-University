"""
В качестве примера была выбрана библиотека NumPy для математических операций

Особенности NumPy:

1. Быстрые математические операции
2. Большой выбор функций
3. Эффективное использование памяти
4. Интеграция с другими библиотеками

"""
import numpy as np

arr = np.arange(1, 11)
print("Массив чисел:", arr)

mean = np.mean(arr)
print("Среднее значение:", mean)

sum_arr = np.var(arr)
print("Дисперсия:", sum_arr)

std_dev = np.std(arr)
print("Стандартное отклонение:", std_dev)

arr_times_two = arr * 2
print("Массив после умножения на 2:", arr_times_two)

A = np.array([[2, 1], [1, 1]])
b = np.array([3, 2])

# Решение системы линейных уравнений Ax = b
y = np.linalg.solve(A, b)
print("Решение системы линейных уравнений Ax = b:", y)

random_matrix = np.random.rand(3, 3)
print("Случайная матрица:", random_matrix)