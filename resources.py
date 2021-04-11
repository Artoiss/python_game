
'Class for taking care of resource management.'
class Resources:
    def __init__(self):
        self.wood = 10
        self.gold = 0
        self.crystal = 0
        self.gather_speed_wood = 1
        self.gather_speed_gold = 1
        self.gather_speed_crystal = 1

    'Returns amount of wood.'
    def show_wood(self):
        return self.wood

    'Returns amount of gold'
    def show_gold(self):
        return self.gold

    'Returns amount of crystal'
    def show_crystal(self):
        return self.crystal

    'Add wood for player usage'
    def add_wood(self):
        self.wood += self.gather_speed_wood

    'Add wood for player usage'
    def add_gold(self):
        self.gold += self.gather_speed_gold

    'Add wood for player usage'
    def add_crystal(self):
        self.crystal += self.gather_speed_crystal

    'If troops are upgraded, improve gathering'
    def improve_wood(self):
        self.gather_speed_wood += 1

    'If troops are upgraded, improve gathering'
    def improve_gold(self):
        self.gather_speed_gold += 1

    'If troops are upgraded, improve gathering'
    def improve_crystal(self):
        self.gather_speed_crystal += 1

    'Check if player has enough wood and use it if has.'
    def use_wood(self, amount):
        if self.wood - amount >= 0:
            self.wood -= amount
            return 1
        else:
            return 0

    'Check if player has enough gold and use it if has.'
    def use_gold(self, amount):
        if self.gold - amount >= 0:
            self.gold -= amount
            return 1
        else:
            return 0

    'Check if player has enough crystal and use it if has.'
    def use_crystal(self, amount):
        if self.crystal - amount >= 0:
            self.crystal -= amount
            return 1
        else:
            return 0