import csv

all_heroes = []

with open("heroes.csv") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        all_heroes.append(row)


def get_hero_name(hero):
    return hero["name"]

for hero in sorted(all_heroes, key=get_hero_name):
    print(hero["name"])


for hero in sorted(all_heroes, key=lambda hero:hero["name"]):
    print(hero["name"])
    