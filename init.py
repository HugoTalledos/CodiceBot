import sys
sys.path.append('.\\utils\\')
sys.path.append('.\\controllers\\')
sys.path.append('.\\drivers\\')

from TelegramBot import TelegramBot
from controllerOption import select_option

bot = TelegramBot('Hugo')

def main(action, message):
  select_option(action, message, bot)

if __name__ == '__main__':
  action = sys.argv[1]
  message = sys.argv[2] if len(sys.argv) == 3 else ''
  main(action, message)