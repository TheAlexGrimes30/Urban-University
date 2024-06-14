import csv
import os


class PriceMachine:

    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def _search_product_price_weight(self, headers, available_product_names, available_price_names, available_weight_names):
        """
        Возвращает имена столбцов с названием товара, ценой и весом.
        :param headers: Заголовки столбцов
        :param available_product_names: Допустимые имена для столбца с названием товара
        :param available_price_names: Допустимые имена для столбца с ценой
        :param available_weight_names: Допустимые имена для столбца с весом
        :return: Имена столбцов (product_col, price_col, weight_col)
        """
        product_col = price_col = weight_col = None
        for header in headers:
            if header in available_product_names:
                product_col = header
            elif header in available_price_names:
                price_col = header
            elif header in available_weight_names:
                weight_col = header
        print(product_col, weight_col, price_col)
        return product_col, price_col, weight_col

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
        :param file_path: Путь к каталогу с файлами
        :return: None
        """
        available_product_names = ['товар', 'название', 'наименование', 'продукт']
        available_price_names = ['розница', 'цена']
        available_weight_names = ['вес', 'масса', 'фасовка']

        for file in os.listdir(file_path):
            if 'price' in file and file.endswith('.csv'):
                with open(os.path.join(file_path, file), newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    product_col, price_col, weight_col = self._search_product_price_weight(
                        reader.fieldnames, available_product_names, available_price_names, available_weight_names)
                    if product_col and price_col and weight_col:
                        for row in reader:
                            try:
                                price_per_kg = float(row[price_col]) / float(row[weight_col])
                                self.data.append({
                                    'name': row[product_col],
                                    'price': float(row[price_col]),
                                    'weight': float(row[weight_col]),
                                    'file': file,
                                    'price_per_kg': price_per_kg
                                })
                            except ValueError:
                                continue

    def export_to_html(self, fname='output.html'):
        """
        Экспортирует данные в HTML файл
        :param fname: Имя выходного HTML файла
        :return: None
        """
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
            <style>
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid black; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
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

        for i, item in enumerate(self.data, 1):
            result += f'''
                <tr>
                    <td>{i}</td>
                    <td>{item['name']}</td>
                    <td>{item['price']}</td>
                    <td>{item['weight']}</td>
                    <td>{item['file']}</td>
                    <td>{item['price_per_kg']}</td>
                </tr>
            '''
        result += '''
            </table>
        </body>
        </html>
        '''
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(result)

    def find_text(self, text):
        """
        Ищет и возвращает список позиций, содержащих указанный текст в названии продукта.
        :param text: Текст для поиска
        :return: Список позиций
        """
        filtered_data = [item for item in self.data if text.lower() in item['name'].lower()]
        filtered_data.sort(key=lambda x: x['price_per_kg'])
        return filtered_data


def main():
    pm = PriceMachine()
    pm.load_prices('data')  # Укажите путь к папке с прайс-листами

    while True:
        user_input = input("Введите текст для поиска (или 'exit' для выхода): ").strip()
        if user_input.lower() == 'exit':
            print("Работа завершена.")
            break
        results = pm.find_text(user_input)
        if results:
            print(f"{'№':<3} {'Наименование':<30} {'Цена':<10} {'Вес':<10} {'Файл':<15} {'Цена за кг.':<10}")
            for i, item in enumerate(results, 1):
                print(f"{i:<3} {item['name']:<30} {item['price']:<10} {item['weight']:<10} {item['file']:<15} {item['price_per_kg']:<10}")
        else:
            print("Товары не найдены.")

    pm.export_to_html('output.html')
    print("Данные экспортированы в output.html")


if __name__ == "__main__":
    main()