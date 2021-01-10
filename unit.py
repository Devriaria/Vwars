from weapon import weapon


class Unit:
    def __init__(self, player, game):
        print("created")
        self.hp = 5
        self.name = player.name
        self.attack_value = weapon.attack_value
        self.alive = True
        self.team = None
        self.player = player
        self.game = game

    def attack(self, targets):
        for target_ in targets:
            self.game.add_string(f"{self.name} нанёс {self.attack_value} урона {target_.name} {weapon.name_text}.\n")
            target_.take_dmg(self.attack_value)

    def take_dmg(self, attack_value):
        self.hp -= attack_value
        if self.hp <= 0:
            self.alive = False


class Team:
    def __init__(self, players_list, game):
        self.units_list = []
        self.game = game
        for player in players_list:
            unit = Unit(player, game)
            unit.team = self
            self.units_list.append(unit)
        self.team_name = players_list[0].name
