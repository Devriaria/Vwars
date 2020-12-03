from bot import AssgardBot
from lobby import Lobby


bot = AssgardBot()


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.from_user.id, "hello")


@bot.message_handler(commands=["start_game"])
def start_game(message):
    lobby = Lobby(message.chat.id)
    bot.lobbies[message.chat.id] = lobby
    bot.send_message(message.chat.id, "Идёт набор в игру. Нажмите /join, чтобы присоединиться")


@bot.message_handler(commands=["join"])
def join_game(message):
    lobby = bot.lobbies[message.chat.id]
    print(lobby)
    lobby.join(message.from_user.id, message.from_user.first_name)


@bot.message_handler(commands=["fight"])
def fight(message):
    lobby = Lobby(message.chat.id)
    game = lobby.create_game()
    game.run()



bot.polling()
