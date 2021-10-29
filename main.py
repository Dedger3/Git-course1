import telebot

BOT_TOKEN = "2061220909:AAFrQlOZG4CDeAJ3wswutXHaihPoKH8PYbw"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def handle_message(message):
    bot.reply_to(message, "Привет")

@bot.message_handler(content_types=["text"])
def handle_message(message):
    bot.reply_to(message, message.text)

bot.polling()