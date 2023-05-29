class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkingSpaces = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:
        limit = self.parkingSpaces[carType]
        
        if limit - 1 < 0:
            return False
        
        self.parkingSpaces[carType] -= 1
        
        return True
