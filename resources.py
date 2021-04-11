
'Class for taking care of resource management.'
class Resources:
    def __init__(self):
        self.wood = 10
        self.gold = 0
        self.crystal = 0

    def show_wood(self):
        return self.wood

    def show_gold(self):
        return self.gold

    def show_crystal(self):
        return self.crystal

    def add_wood(self, amount):
        self.wood += amount