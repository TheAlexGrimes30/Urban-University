import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill

    def run(self):
        print(f"{self.name}, на нас напали")
        enemies = 100
        days = 0
        while enemies > 0:
            days += 1
            enemies -= self.skill
            if enemies < 0:
                enemies = 0
            print(f"{self.name}, сражается {days} день(дня) ...,"
                  f"осталось {enemies} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {days} дней!")

knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galand", 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
