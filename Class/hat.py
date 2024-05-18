import random

class Hat:
    house_list = ["Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw"]
    cow = 1

    def __init__(self, name) :
        self.name = name

    @classmethod
    def get_house(cls):
        print(f"House: {random.choice(cls.house_list)}")
        cls.cow += 1
        print(cls.cow)
    


Hat.get_house()

hat1 = Hat("hat1")
hat1.get_house()


hat2 = Hat("hat2")
hat2.get_house()
