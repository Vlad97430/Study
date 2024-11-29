import telebot

bot = telebot.TeleBot('7716662076:AAFxmPPvFg2KY9Qd9yzikXteeqB8VBkGGFg')

@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()