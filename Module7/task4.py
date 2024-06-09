import os
import time

directory = os.getcwd()

for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        filepath = os.path.join(dirpath, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath},'
            f' Размер: {filesize} байт,'
            f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
