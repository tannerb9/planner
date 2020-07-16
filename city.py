class City:

    def __init__(self, name, mayor, year_created):
        self.name = name
        self.mayor = mayor
        self.year_created = year_created
        self.buildings = []

    def add_building(self):
        self.buildings.append(self)
