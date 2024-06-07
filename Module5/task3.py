class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return (self.numberOfFloors == other.numberOfFloors and
                    self.buildingType == other.buildingType)
        return False

building1 = Building(10, 'ЖК')
building2 = Building(10, 'ЖК')
building3 = Building(20, 'Офис')

print(building1 == building2)
print(building1 == building3)
print(building2 == building3)
