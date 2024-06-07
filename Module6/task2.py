class Vehicle:
    vehicle_type: str = None


class Car:
    price: int = 1000000

    def horse_powers(self):
        return 100


class Nissan(Vehicle, Car):
    price: int = 800000
    vehicle_type: str = "Car"

    def horse_powers(self):
        return 120

nissan = Nissan()
print(f"Price: {nissan.price}. Vehicle Type: {nissan.vehicle_type}. Horse Powers: {nissan.horse_powers()}")
