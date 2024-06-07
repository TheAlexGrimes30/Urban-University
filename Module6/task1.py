class Car:
    price = 1000000

    def horse_powers(self):
        return 100


class Nissan(Car):
    price = 800000

    def horse_powers(self):
        return 120


class Kia(Car):
    price = 1200000

    def horse_powers(self):
        return 110


car = Car()
print(f"Цена автомобиля: {car.price}, лошадиные силы: {car.horse_powers()}")

nissan = Nissan()
print(f"Цена автомобиля Nissan: {nissan.price}, лошадиные силы Nissan: {nissan.horse_powers()}")

kia = Kia()
print(f"Цена автомобиля Kia: {kia.price}, лошадиные силы Kia: {kia.horse_powers()}")
