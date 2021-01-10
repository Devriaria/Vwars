import random
from unit import Unit, Team
from bot import AssgardBot
from weapon import weapon


class Game:
    def __init__(self, lobby_teams, chat_id):
        self.teams = []
        self.chat_id = chat_id
        self.round_string = ""
        self.round_count = 0
        for team in lobby_teams:
            self.teams.append(Team(team, self))

    def add_string(self, string):
        self.round_string += string

    def send_string(self):
        AssgardBot().send_message(self.chat_id, self.round_string)
        self.round_string = ""

    def run(self):
        self.wait_players_turn()
        self.make_turn()
        self.players_alive()
        self.remove_dead()
        if self.check_end():
            self.end()
        else:
            self.run()

    def wait_players_turn(self):
        if self.round_count == 0:
            print("Оружие выбрано:")
            for team_ in self.teams:
                for player in team_.units_list:
                    print(f"Оружие {player.name} - {weapon.name}")

    def make_turn(self):
        self.round_count += 1
        self.add_string(f"Раунд {self.round_count}\n\n")
        for team_ in self.teams:
            for player in team_.units_list:
                if player in self.teams[0].units_list:
                    targets = self.teams[1].units_list
                    random_target = random.choice(targets)
                    player.attack([random_target])
                else:
                    player.attack(self.teams[0].units_list)

    def players_alive(self):
        for team_ in self.teams:
            for player in team_.units_list:
                self.add_string(f"У {player.name} осталось {player.hp} жизней.\n")

    def remove_dead(self):
        for team_ in self.teams:
            for player in team_.units_list:
                if not player.alive:
                    player.team.units_list.remove(player)
                    self.add_string(f"{player.name} умер.\n")

    def check_end(self):
        self.send_string()
        if not any(team_.units_list for team_ in self.teams):
            AssgardBot().send_message(self.chat_id, "Обе команды проиграли.")
            return True
        else:
            for team_ in self.teams:
                if not team_.units_list:
                    AssgardBot().send_message(self.chat_id, f"Команда {team_.team_name} проиграла.")
                    return True
        return False

    def end(self):
        pass
