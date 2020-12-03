from bot import AssgardBot
from main import Game


class Lobby:
    def __init__(self, chat_id):
        self.players = []
        self.chat_id = chat_id
        self.teams = []

    def join(self, user_id, name):
        player = Player(user_id, name, self)
        print(name)
        if not any(user_id == player.user_id for player in self.players):
            self.players.append(player)
            if len(self.players) == 1:
                self.teams.append([player])
                player.team = 0
                AssgardBot().send_message(self.chat_id, f"{player.name} присоединился к {player.team}")
            elif len(self.players) == 2:
                self.teams.append([player])
                player.team = 1
                AssgardBot().send_message(self.chat_id, f"{player.name} присоединился к {player.team}")
            else:
                self.ask_team(player)
            for i in range(len(self.teams)):
                print(self.teams[i])

    def ask_team(self, player):
        pass

    def create_game(self):
        game = Game(chat_id=self.chat_id, lobby_teams=self.teams)
        AssgardBot.games[self.chat_id] = game
        return game


class Player:
    def __init__(self, user_id, name, lobby):
        self.user_id = user_id
        self.team = None
        self.name = name
        self.lobby = lobby
