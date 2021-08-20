from switch import switch
class Helper:
  def get_help(action, bot):
    with switch(action) as s:
      if s.case('s', True):
        bot.send_message('help-s')
      if s.case('pa', True):
        bot.send_message('help-pa')
      if s.case('pe', True):
        bot.send_message('help-pe')
      if s.case('pd', True):
        bot.send_message('help-pd')
      if s.case('ps', True):
        bot.send_message('help-ps')
      if s.case('pas', True):
        bot.send_message('help-pas')
      if s.default():
        bot.send_message('help-h')