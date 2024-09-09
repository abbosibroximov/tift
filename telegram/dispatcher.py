from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler
import os
from .handlers import commands


BOT_TOKEN = os.getenv("6710319872:AAFnaDLqgxp7Btp7ziO5Gm1Qp8OMz0U5hDE")
bot = Bot(token=BOT_TOKEN)

dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("Start", commands.start))

