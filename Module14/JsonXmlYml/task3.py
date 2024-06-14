import json
import os


def employees_rewrite(sort_type):
    """
    Сортирует данные сотрудников по указанному ключу и сохраняет в новый JSON-файл.

    :param sort_type: Ключ для сортировки (например, 'lastName', 'department', 'salary')
    :raises ValueError: Если передан неверный ключ для сортировки
    """

    sort_type_lower = sort_type.lower()

    # Поддерживаемые ключи сортировки
    valid_keys = ['firstname', 'lastname', 'department', 'salary']

    if sort_type_lower not in valid_keys:
        raise ValueError('Bad key for sorting')

    with open('employees.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if sort_type_lower == 'salary':
        sorted_employees = sorted(data['employees'], key=lambda x: x[sort_type], reverse=True)
    else:
        sorted_employees = sorted(data['employees'], key=lambda x: x[sort_type].lower())

    sorted_data = {'employees': sorted_employees}

    output_filename = f'employees_{sort_type_lower}_sorted.json'
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(sorted_data, file, indent=4, ensure_ascii=False)

    print(f'Data sorted by {sort_type} and saved to {output_filename}')


try:
    employees_rewrite('lastName')
    employees_rewrite('department')
    employees_rewrite('salary')
    employees_rewrite('firstName')
except ValueError as e:
    print(e)