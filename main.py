import random
from unit import Unit, Team
from bot import AssgardBot


class Game:
    def __init__(self, lobby_teams, chat_id):
        self.teams = []
        self.chat_id = chat_id
        for team in lobby_teams:
            self.teams.append(Team(team))

    def run(self):
        self.wait_players_turn()
        self.make_turn()
        self.remove_dead()
        if self.check_end():
            self.end()
        else:
            self.run()

    def wait_players_turn(self):
        pass

    def make_turn(self):
        for team_ in self.teams:
            for player in team_.units_list:
                if player in self.teams[0].units_list:
                    targets = self.teams[1].units_list
                    random_target = random.choice(targets)
                    player.attack([random_target])
                else:
                    player.attack(self.teams[0].units_list)

    def remove_dead(self):
        for team_ in self.teams:
            for player in team_.units_list:
                AssgardBot().send_message(self.chat_id, f"У игрока {player.name} осталось {player.hp} жизней.")
                if not player.alive:
                    player.team.units_list.remove(player)
                    AssgardBot().send_message(self.chat_id, f"Игрок {player.name} умер.")

    def check_end(self):
        for team_ in self.teams:
            if not team_.units_list:
                AssgardBot().send_message(self.chat_id, f"Команда {team_.team_name} проиграла.")
                return True
        return False

    def end(self):
        pass