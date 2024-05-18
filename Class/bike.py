class Bike:
    
    def __init__(self, name, bike_type):
        self._name = None
        self._bike_type = None
        self.name = name
        self.bike_type = bike_type 

    
    def __str__(self) -> str:
        return f"Bike Name: {self._name}\nBike Type: {self.bike_type}"
    

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "hello":
            raise ValueError("Invalid name")
        self._name = name

    @property
    def bike_type(self):
        return self._bike_type

    @bike_type.setter
    def bike_type(self, bike_type):
        if bike_type not in ["Standard", "Cruiser", "Sport"]:
            raise ValueError("Invalid Bike Type")
        self._bike_type = bike_type


def main():
    bike1 = Bike("Hero Honda", "Standard")
    print(bike1)

    bike2 = Bike("Shallow", "Cruiser")
    bike2.bike_type = "Sport"
    print(bike2)



main()