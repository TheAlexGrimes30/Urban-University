from multiprocessing import Process, Queue

def producer(queue):
    for i in range(5):
        data = f"Data {i}"
        queue.put(data)
        print(f"Produced: {data}")

def consumer(queue):
    while True:
        data = queue.get()
        print(f"Consumed: {data}")

if __name__ == '__main__':
    queue = Queue()

    producer_process = Process(target=producer, args=(queue,))
    consumer_process = Process(target=consumer, args=(queue,))

    consumer_process.start()  # Запускаем потребителя сначала
    producer_process.start()

    producer_process.join()
    consumer_process.terminate()