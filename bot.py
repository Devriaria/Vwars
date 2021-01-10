import telebot


class AssgardBot(telebot.TeleBot):
    games = {}
    lobbies = {}

    def __init__(self):
        telebot.TeleBot.__init__(self, "1430869875:AAFCmixexSg45PniBqiwkDNsIcfkJLe6ROY")

    def keyboard(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton(text="Кнопка", callback_data="01")
        keyboard.add(button)
        return keyboard
