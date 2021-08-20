import telebot
import os
from dotenv import load_dotenv

from common import config
class TelegramBot:
  def __init__(self, bossName):
    load_dotenv()
    tokenTelegram = os.getenv('TOKEN_TELEGRAM')
    chatId = os.getenv('CHAT_ID')
    self._bossName = bossName

    self._token = tokenTelegram
    self._chatID = chatId

    self.bot = telebot.TeleBot(tokenTelegram, parse_mode=None)

  def send_message(self, message, chatId = ""):
    text = config().get(message) if config().get(message) else message
    self.bot.send_message(chatId or self._chatID, '{} {}'.format(self._bossName, text))

  def active_webhook(self, urlBase):
    self.bot.set_webhook(url="{}/webhook/{}".format(urlBase, self._token),
                         allowed_updates=["message"])

  def get_chatId(self):
    return int(self._chatID)

  def get_boss_name(self):
    return self._bossName

  def set_boss_name(self, name):
    self._bossName = name
