from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
import settings
from datetime import date
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

planet_list=['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
def planet(bot,update):
    text = 'Вызван /planet'
    print(text)
    update.message.reply_text(text)
    today=str(date.today())
    today.replace('-', '/')
    user_text = update.message.text 
    print(user_text)
    user_list=user_text.split(' ')
    for plan in planet_list:
        if plan in user_list:
            planet_object=getattr(ephem, plan)
            res=planet_object(today)
            ephem.constellation(res)
            update.message.reply_text(ephem.constellation(res))


def main():
    mybot=Updater(settings.KEY, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()