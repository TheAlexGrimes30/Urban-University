from multiprocessing import Process, Pipe

def sender(conn):
    for i in range(5):
        data = f"Data {i}"
        conn.send(data)
        print(f"Sent: {data}")

def receiver(conn):
    while True:
        data = conn.recv()
        print(f"Received: {data}")

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    sender_process = Process(target=sender, args=(parent_conn,))
    receiver_process = Process(target=receiver, args=(child_conn,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.terminate()