import irclib
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('bot.cfg')

irc_server = config.get('irc_server_settings','irc_server')
irc_port = config.get('irc_server_settings','irc_port')

bot_nick = config.get('bot_settings','bot_nick')
bot_ident = config.get('bot_settings','bot_ident')
bot_real_name = config.get('bot_settings','bot_real_name')
bot_owner = config.get('bot_settings','bot_owner')
bot_autojoin_channels = config.get('bot_settings','bot_autojoin_channels')

myirc = irclib.irc(irc_server,irc_port,bot_nick,bot_ident,bot_real_name,bot_autojoin_channels)
myirc.connect()

