import telebot


class AssgardBot(telebot.TeleBot):
    games = {}
    lobbies = {}

    def __init__(self):
        telebot.TeleBot.__init__(self, "1430869875:AAFCmixexSg45PniBqiwkDNsIcfkJLe6ROY")
