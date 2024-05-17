import csv

with open("heroes.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "hero_type"])
    for _ in range(2):
        name = input("Enter hero name: ").rstrip()
        hero_type = input("Enter hero type: ").rstrip()
        print("")
        writer.writerow({"name": name, "hero_type": hero_type})

    

    