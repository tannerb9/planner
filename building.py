from datetime import date


class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = date.today()

    def purchase(self, buyer_name):
        self.owner = buyer_name
