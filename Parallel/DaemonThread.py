import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)

if __name__ == '__main__':
    thread1 = threading.Thread(target=print_numbers, daemon=True)
    thread2 = threading.Thread(target=print_letters, daemon=True)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Python")