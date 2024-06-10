import threading
import time
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(threading.Thread):
    def __init__(self, number, cafe, queue):
        super().__init__()
        self.number = number
        self.cafe = cafe
        self.queue = queue

    def run(self):
        self.cafe.serve_customer(self)


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            print(f"Посетитель номер {customer_number} прибыл.")
            customer = Customer(customer_number, self, self.queue)
            self.queue.put(customer)
            customer_number += 1
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
                time.sleep(5)  # время обслуживания
                print(f"Посетитель номер {customer.number} покушал и ушёл.")
                table.is_busy = False
                return
        else:
            print(f"Посетитель номер {customer.number} ожидает свободный стол.")
            self.queue.put(customer)


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

while True:
    try:
        customer = cafe.queue.get(timeout=1)
        customer.start()
    except queue.Empty:
        if not any(table.is_busy for table in cafe.tables):
            break

customer_arrival_thread.join()
