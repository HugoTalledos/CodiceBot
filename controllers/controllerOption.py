from switch import switch
from Manager import Manager
from Message import Message
from Helper import Helper

manager = Manager()

def select_option(action, message, bot):
  with switch(action, comparator=lambda x, y: x in y) as a:
    if a.case(('s', '/s'), True):
      Message.sendMessage(message, bot)
    if a.case(('pa', '/pa'), True):
      manager.add_password(message, bot)
    if a.case(('pe', '/pe'), True):
      manager.edit_password(message, bot)
    if a.case(('pd', '/pd'), True):
      manager.delete_password(message, bot)
    if a.case(('ps', '/ps'), True):
      manager.get_password(message, bot)
    if a.case(('pas', '/pas'), True):
      manager.get_services(bot)
    if a.case(('h', '/h'), True):
      Helper.get_help(message, bot)
    if a.case(('w'), True):
      bot.active_webhook(message)
    if a.default():
      bot.send_message('default')