class House:
    def __init__(self):
        self.number_of_floors = 0

    def setNewNumberOfFloors(self, floors):
        self.number_of_floors = floors

house = House()
print(house.number_of_floors)

house.setNewNumberOfFloors(10)
print(house.number_of_floors)