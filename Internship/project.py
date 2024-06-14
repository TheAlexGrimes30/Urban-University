import csv
import os
import json


class PriceMachine():

    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def load_prices(self, file_path=''):
        """
        Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт

            Допустимые названия для столбца с ценой:
                розница
                цена

            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        :param file_path:
        :return:
        """

        available_product_names = ['товар', 'название', 'наименование', 'продукт']
        available_price_names = ['розница', 'цена']
        available_weight_names = ['вес', 'масса', 'фасовка']

        for file in os.listdir(file_path):
            if 'price' in file and file.endswith('.csv'):
                reader = csv.DictReader(file, delimiter=';')
                headers = reader.fieldnames
                for header in headers:
                    if header in available_product_names:
                        pass
                    if header in available_price_names:
                        pass
                    if header in available_weight_names:
                        pass

    def _search_product_price_weight(self, headers):
        '''
            Возвращает номера столбцов
        '''

    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''

    def find_text(self, text):
        pass


pm = PriceMachine()
print(pm.load_prices())

'''
    Логика работы программы
'''
print('the end')
print(pm.export_to_html())