from building import Building
from city import City

building_one = Building("5 Pennies Ln", 5)
building_one.construct()
building_one.purchase("Mighty Man")

building_two = Building("3 Yard St", 3)
building_two.construct()
building_two.purchase("Mighty Man")

building_three = Building("0 Candy Ave", 10)
building_three.construct()
building_three.purchase("Mighty Man")

building_four = Building("6 Lap Blvd", 20)
building_four.construct()
building_four.purchase("Mighty Man")

building_five = Building("9 Freed Way", 9)
building_five.construct()
building_five.purchase("Mighty Man")


megalopolis = City("Megalopolis", "Megamind", 2020)
megalopolis.buildings.append(building_one)
megalopolis.buildings.append(building_two)
megalopolis.buildings.append(building_three)
megalopolis.buildings.append(building_four)
megalopolis.buildings.append(building_five)

for building in megalopolis.buildings:
    print(building.__dict__)
