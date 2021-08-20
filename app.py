from flask import Flask, request
import logging
import sys
sys.path.append('.\\utils\\')
sys.path.append('.\\controllers\\')
sys.path.append('.\\drivers\\')
import os
from dotenv import load_dotenv
from TelegramBot import TelegramBot
from controllerOption import select_option

bot = TelegramBot('Hugo')
load_dotenv()
tokenTelegram = os.getenv('TOKEN_TELEGRAM')
route = '/webhook/{}'.format(tokenTelegram)
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route(route, methods=['POST'])
def telegram_webhook():
  data = request.json
  userDeleted = data.get('my_chat_member')
  print(userDeleted)
  if userDeleted is None:
    chat_id = data['message']['chat']['id']
    first_name = data['message']['chat']['first_name']
    message = data['message']['text']
    print(chat_id)
    if chat_id != bot.get_chatId():
      bot.set_boss_name(first_name)
      bot.send_message('unknown-user', chat_id)
    else: 
      action = message.split(' ')[0]
      content = message.split(' ')[1] if len(message.split(' ')) > 1 else ''
      bot.set_boss_name(first_name)
      select_option(action, content, bot)
      
  return ''

if __name__ == '__main__':
	app.run(host='0.0.0.0')
