import queue
import threading
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
        self.lock = threading.Lock()


class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()
        self.condition = threading.Condition()
        self.customers_served = 0

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            print(f"Посетитель номер {customer_number} прибыл.")
            customer = Customer(customer_number, self)
            self.queue.put(customer)
            customer_number += 1
            time.sleep(1)

    def serve_customer(self, customer):
        with self.condition:
            served = False
            while not served:
                for table in self.tables:
                    if not table.is_busy:
                        with table.lock:
                            if not table.is_busy:
                                table.is_busy = True
                                print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
                                served = True
                                break
                if not served:
                    print(f"Посетитель номер {customer.number} ожидает свободный стол.")
                    self.condition.wait()
            time.sleep(3)
            with table.lock:
                table.is_busy = False
                print(f"Посетитель номер {customer.number} покушал и ушёл.")
            self.condition.notify_all()
            with self.condition:
                self.customers_served += 1


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

while customer_arrival_thread.is_alive() or not cafe.queue.empty() or cafe.customers_served < 20:
    try:
        customer = cafe.queue.get(timeout=1)
        customer.start()
    except queue.Empty:
        pass

customer_arrival_thread.join()

for table in tables:
    if table.is_busy:
        table.lock.acquire()
