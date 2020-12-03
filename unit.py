class Unit:
    def __init__(self, player):
        print("created")
        self.hp = 5
        self.name = player.name
        self.attack_value = 2
        self.alive = True
        self.team = None

    def attack(self, targets):
        for target_ in targets:
            print(f"Игрок {self.name} нанёс {self.attack_value} урона {target_.name}.")
            target_.take_dmg(self.attack_value)

    def take_dmg(self, attack_value):
        self.hp -= attack_value
        if self.hp <= 0:
            self.alive = False


class Team:
    def __init__(self, players_list):
        self.units_list = []
        for player in players_list:
            unit = Unit(player)
            unit.team = self
        self.team_name = players_list[0].name
