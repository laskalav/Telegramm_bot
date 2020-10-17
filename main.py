import config
import telebot
from random import randrange
bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def dice_drop(message: telebot.types.Message):
    if "кубик" in message.text.lower():
        # bot.send_message(message.chat.id, randrange(1,7))
        res = ([
            randrange(1, int(i) + 1)
            for i in message.text.split(" ")
            if i.isdigit()
        ])
        print(res)
        bot.send_message(message.chat.id, " ".join([str(i) for i in res]) or randrange(1, 7))


if __name__ == '__main__':
    bot.polling(none_stop=True)
